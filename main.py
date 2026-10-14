import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QMessageBox,
    QTableWidgetItem, QHeaderView, QLabel
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

from ui_login import Ui_MainWindow as LoginUI
from ui_autorazation import Ui_MainWindow as CatalogUI
from ui_cart import Ui_CartDialog as CartUI
from ui_orders import Ui_OrdersDialog as OrdersUI

from database import (
    check_user, fetch_categories, fetch_products,
    save_order, fetch_orders, fetch_order_details, remove_order
)


# ============================================================
# ОКНО КОРЗИНЫ
# ============================================================
class CartWindow(QWidget):
    """Окно корзины и оформления заказа."""

    def __init__(self, user_data, items, catalog_ref):
        super().__init__()
        self.ui = CartUI()
        self.ui.setupUi(self)

        self.user_data = user_data
        self.items = items
        self.catalog_ref = catalog_ref
        self.total_sum = 0.0

        self._bind_buttons()
        self._render_table()

    def _bind_buttons(self):
        self.ui.backButton.clicked.connect(self.close)
        self.ui.clearCartButton.clicked.connect(self._clear_all)
        self.ui.removeItemButton.clicked.connect(self._remove_selected)
        self.ui.checkoutButton.clicked.connect(self._checkout)

    def _render_table(self):
        columns = ["ID", "Наименование", "Цена (руб.)", "Кол-во", "Сумма (руб.)"]
        table = self.ui.cartTable
        table.setColumnCount(len(columns))
        table.setHorizontalHeaderLabels(columns)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.setRowCount(0)

        total = 0.0
        for idx, item in enumerate(self.items):
            # item = [product_id, name, price, qty, sum]
            table.insertRow(idx)
            row_sum = item[2] * item[3]
            item[4] = row_sum
            total += row_sum

            table.setItem(idx, 0, QTableWidgetItem(str(item[0])))
            table.setItem(idx, 1, QTableWidgetItem(str(item[1])))
            table.setItem(idx, 2, QTableWidgetItem(f"{item[2]:.2f}"))
            table.setItem(idx, 3, QTableWidgetItem(str(item[3])))
            table.setItem(idx, 4, QTableWidgetItem(f"{row_sum:.2f}"))

        pretty_total = f"{total:,.2f}".replace(",", " ")
        self.ui.totalPriceLabel.setText(f"Итого к оплате: {pretty_total} руб.")
        self.total_sum = total

    def _remove_selected(self):
        row = self.ui.cartTable.currentRow()
        if row < 0:
            QMessageBox.warning(self, "Внимание", "Выберите строку для удаления!")
            return
        self.items.pop(row)
        self._render_table()

    def _clear_all(self):
        self.items.clear()
        self._render_table()

    def _checkout(self):
        if not self.items:
            QMessageBox.warning(self, "Ошибка", "Корзина пуста!")
            return

        fio = self.user_data.get("fio", "Анонимный клиент")
        if save_order(fio, self.items, self.total_sum):
            QMessageBox.information(self, "Успех", "Заказ успешно оформлен!")
            self.items.clear()
            self.catalog_ref.cart = []
            self.close()
        else:
            QMessageBox.critical(self, "Ошибка", "Не удалось сохранить заказ в БД.")


# ============================================================
# ОКНО ЗАКАЗОВ
# ============================================================
class OrdersWindow(QWidget):
    """Окно управления заказами."""

    def __init__(self, user_data):
        super().__init__()
        self.ui = OrdersUI()
        self.ui.setupUi(self)
        self.user_data = user_data

        self._bind_buttons()
        self._configure_permissions()
        self._load_orders()

    def _bind_buttons(self):
        self.ui.backButton.clicked.connect(self.close)
        self.ui.deleteOrderButton.clicked.connect(self._delete_selected)
        self.ui.ordersTable.itemSelectionChanged.connect(self._show_details)

    def _configure_permissions(self):
        role_id = self.user_data.get("role_id", 0)
        if role_id != 3:
            self.ui.editOrderButton.hide()

    def _load_orders(self):
        data = fetch_orders()
        headers = ["ID Заказа", "Дата", "Клиент", "Сумма"]
        table = self.ui.ordersTable
        table.setColumnCount(len(headers))
        table.setHorizontalHeaderLabels(headers)

        if not data:
            table.setRowCount(0)
            return

        table.setRowCount(len(data))

        for r_idx, row_data in enumerate(data):
            for c_idx, val in enumerate(row_data):
                text = self._format_cell(c_idx, val)
                cell = QTableWidgetItem(text)
                cell.setFlags(cell.flags() ^ Qt.ItemIsEditable)
                table.setItem(r_idx, c_idx, cell)

        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    @staticmethod
    def _format_cell(col_index, value):
        if col_index == 3:
            if value is None:
                return "0.00 ₽"
            try:
                return f"{float(value):,.2f}".replace(",", " ") + " ₽"
            except (ValueError, TypeError):
                return str(value)
        return str(value) if value is not None else "—"

    def _show_details(self):
        row = self.ui.ordersTable.currentRow()
        if row < 0:
            return

        order_id = int(self.ui.ordersTable.item(row, 0).text())
        details = fetch_order_details(order_id)

        headers = ["Наименование товара", "Количество", "Цена за ед.", "Сумма"]
        table = self.ui.orderDetailsTable
        table.setColumnCount(len(headers))
        table.setHorizontalHeaderLabels(headers)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.setRowCount(0)

        for r_idx, item in enumerate(details):
            table.insertRow(r_idx)
            for c_idx, val in enumerate(item):
                if c_idx in (2, 3):
                    text = f"{val:,.2f}".replace(",", " ")
                else:
                    text = str(val)
                table.setItem(r_idx, c_idx, QTableWidgetItem(text))

    def _delete_selected(self):
        row = self.ui.ordersTable.currentRow()
        if row < 0:
            QMessageBox.warning(self, "Внимание", "Выберите заказ для удаления!")
            return

        order_id = int(self.ui.ordersTable.item(row, 0).text())
        answer = QMessageBox.question(
            self, "Подтверждение",
            f"Удалить заказ №{order_id}?",
            QMessageBox.Yes | QMessageBox.No
        )

        if answer == QMessageBox.Yes:
            if remove_order(order_id):
                QMessageBox.information(self, "Успех", "Заказ удален!")
                self._load_orders()
                self.ui.orderDetailsTable.setRowCount(0)
            else:
                QMessageBox.critical(self, "Ошибка", "Не удалось удалить заказ.")


# ============================================================
# ОКНО КАТАЛОГА
# ============================================================
class CatalogWindow(QMainWindow):
    """Главное окно каталога товаров."""

    def __init__(self, user_data):
        super().__init__()
        self.ui = CatalogUI()
        self.ui.setupUi(self)

        self.user_data = user_data
        self.products = []
        self.cart = []

        self._bind_buttons()
        self._apply_permissions()
        self._load_catalog()

    def _bind_buttons(self):
        fio = self.user_data.get("fio", "Гость")
        role = self.user_data.get("role_name", "Неавторизованный")
        self.ui.userinfolabel.setText(f"{fio} ({role})")

        self.ui.LogoutButton.clicked.connect(self._logout)
        self.ui.addToOrderButton.clicked.connect(self._add_to_cart)
        self.ui.manageOrdersButton.clicked.connect(self._open_orders)

        self.ui.searchLineEdit.textChanged.connect(self._apply_filters)
        self.ui.filterComboBox.currentTextChanged.connect(self._apply_filters)
        self.ui.sortComboBox.currentIndexChanged.connect(self._apply_filters)

    def _apply_permissions(self):
        role_id = self.user_data.get("role_id", 0)
        if role_id == 0:
            self.ui.addToOrderButton.hide()
            self.ui.manageOrdersButton.hide()
        elif role_id == 1:
            self.ui.addToOrderButton.show()
            self.ui.manageOrdersButton.hide()
        elif role_id in (2, 3):
            self.ui.addToOrderButton.show()
            self.ui.manageOrdersButton.show()

    def _load_catalog(self):
        headers = [
            "Фото", "Наименование", "Категория", "Подкатегория",
            "Производитель", "Состав", "Цена (руб.)", "Остаток"
        ]
        table = self.ui.productsTable
        table.setColumnCount(len(headers))
        table.setHorizontalHeaderLabels(headers)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.ui.sortComboBox.clear()
        self.ui.sortComboBox.addItems(["Без сортировки", "Сначала дешевые", "Сначала дорогие"])

        self.ui.filterComboBox.clear()
        self.ui.filterComboBox.addItem("Все категории")
        self.ui.filterComboBox.addItems(fetch_categories())

        self.products = fetch_products()
        self._apply_filters()

    def _apply_filters(self):
        query = self.ui.searchLineEdit.text().lower().strip()
        category = self.ui.filterComboBox.currentText()
        sort_idx = self.ui.sortComboBox.currentIndex()

        result = []
        for row in self.products:
            p_id, name, cat, subcat, manuf, comp, price, qty = row

            if query and not (query in name.lower() or query in manuf.lower()):
                continue
            if category != "Все категории" and cat != category:
                continue

            result.append(row)

        if sort_idx == 1:
            result.sort(key=lambda x: x[6])
        elif sort_idx == 2:
            result.sort(key=lambda x: x[6], reverse=True)

        self._render_products(result)

    def _render_products(self, items):
        table = self.ui.productsTable
        table.setRowCount(0)

        for r_idx, item in enumerate(items):
            table.insertRow(r_idx)
            p_id, name, cat, subcat, manuf, comp, price, qty = item

            image_cell = QLabel()
            image_cell.setAlignment(Qt.AlignCenter)
            pixmap = QPixmap(f"images/{p_id}.png")

            if pixmap.isNull():
                image_cell.setText("Нет фото")
            else:
                image_cell.setPixmap(pixmap.scaled(
                    100, 100,
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation
                ))

            image_cell.setProperty("product_id", p_id)
            table.setCellWidget(r_idx, 0, image_cell)

            values = [name, cat, subcat, manuf, comp, price, qty]
            for c_idx, val in enumerate(values, start=1):
                if c_idx == 6:
                    text = f"{val:,.2f}".replace(",", " ")
                else:
                    text = str(val)

                cell = QTableWidgetItem(text)
                cell.setFlags(cell.flags() ^ Qt.ItemIsEditable)

                if c_idx in (6, 7):
                    cell.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)

                table.setItem(r_idx, c_idx, cell)

            table.setRowHeight(r_idx, 110)

    def _add_to_cart(self):
        row = self.ui.productsTable.currentRow()
        if row >= 0:
            label = self.ui.productsTable.cellWidget(row, 0)
            pid = int(label.property("product_id"))
            name = self.ui.productsTable.item(row, 1).text()
            raw_price = self.ui.productsTable.item(row, 6).text().replace(" ", "").replace(",", ".")
            price = float(raw_price)

            updated = False
            for entry in self.cart:
                if entry[0] == pid:
                    entry[3] += 1
                    updated = True
                    break

            if not updated:
                self.cart.append([pid, name, price, 1, price])

        self.cart_window = CartWindow(self.user_data, self.cart, self)
        self.cart_window.show()

    def _open_orders(self):
        self.orders_window = OrdersWindow(self.user_data)
        self.orders_window.show()

    def _logout(self):
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()


# ============================================================
# ОКНО АВТОРИЗАЦИИ
# ============================================================
class LoginWindow(QMainWindow):
    """Окно входа в систему."""

    def __init__(self):
        super().__init__()
        self.ui = LoginUI()
        self.ui.setupUi(self)

        self.ui.loginButton.clicked.connect(self._login)
        self.ui.guestButton.clicked.connect(self._login_as_guest)

    def _login(self):
        login = self.ui.loginLineEdit_2.text().strip()
        if not login:
            QMessageBox.warning(self, "Ошибка", "Введите логин!")
            return

        user = check_user(login)
        if user:
            self._open_catalog(user)
        else:
            QMessageBox.critical(self, "Ошибка", "Пользователь не найден!")

    def _login_as_guest(self):
        guest = {
            "fio": "Гость",
            "role_name": "Неавторизованный пользователь",
            "role_id": 0
        }
        self._open_catalog(guest)

    def _open_catalog(self, user_data):
        self.catalog = CatalogWindow(user_data)
        self.catalog.show()
        self.close()


# ============================================================
# ТОЧКА ВХОДА
# ============================================================
def main():
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()