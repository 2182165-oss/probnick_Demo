# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cart.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QSize, QMetaObject
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import (
    QHBoxLayout, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget
)


class Ui_CartDialog(object):
    """Интерфейс окна корзины."""

    def setupUi(self, CartDialog):
        if not CartDialog.objectName():
            CartDialog.setObjectName("CartDialog")
        CartDialog.resize(800, 600)
        CartDialog.setMinimumSize(QSize(800, 600))
        CartDialog.setMaximumSize(QSize(800, 600))

        window_icon = QIcon()
        window_icon.addFile(
            "programming_course-main/Прил_2_ОЗ_КИМ_09.02.07-2-2027/Images/Чудо Обувь.png",
            QSize(), QIcon.Normal, QIcon.Off
        )
        CartDialog.setWindowIcon(window_icon)

        self.verticalLayout = QVBoxLayout(CartDialog)
        self.verticalLayout.setObjectName("verticalLayout")

        # ---------- Верхняя панель: логотип и заголовок ----------
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.logoLabel = QLabel(CartDialog)
        self.logoLabel.setObjectName("logoLabel")
        self.logoLabel.setMaximumSize(QSize(64, 64))
        self.logoLabel.setPixmap(QPixmap("../Рабочий стол/Images/Чудо Обувь.ico"))
        self.logoLabel.setScaledContents(True)
        self.horizontalLayout_3.addWidget(self.logoLabel)

        self.horizontalSpacer_2 = QSpacerItem(
            188, 20,
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.titleLabel = QLabel(CartDialog)
        self.titleLabel.setObjectName("titleLabel")
        self.titleLabel.setStyleSheet(
            "QLabel#titleLabel {\n"
            "font-family: 'Calibri';\n"
            "font-size: 16pt;\n"
            "font-weight: bold;\n"
            "color: #70B2AF;\n"
            "}\n"
        )
        self.horizontalLayout_3.addWidget(self.titleLabel)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        # ---------- Таблица товаров в корзине ----------
        self.cartTable = QTableWidget(CartDialog)
        self.cartTable.setObjectName("cartTable")
        self.verticalLayout.addWidget(self.cartTable)

        # ---------- Строка с итоговой суммой ----------
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.horizontalSpacer = QSpacerItem(
            98, 20,
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.totalPriceLabel = QLabel(CartDialog)
        self.totalPriceLabel.setObjectName("totalPriceLabel")
        self.totalPriceLabel.setStyleSheet(
            "QLabel#totalPriceLabel {\n"
            "font-family: 'Calibri';\n"
            "font-size: 14pt;\n"
            "font-weight: bold;\n"
            "}"
        )
        self.horizontalLayout_2.addWidget(self.totalPriceLabel)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        # ---------- Кнопки управления корзиной ----------
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        button_style = (
            "QPushButton {\n"
            "background-color: #70B2AF;\n"
            "color: #FFFFFF;\n"
            "border: none;\n"
            "padding: 8px 16px;\n"
            "font-family: 'Calibri';\n"
            "font-size: 12pt;\n"
            "font-weight: bold;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "background-color: #4A8582;\n"
            "}\n"
        )

        self.removeItemButton = QPushButton(CartDialog)
        self.removeItemButton.setObjectName("removeItemButton")
        self.removeItemButton.setStyleSheet(
            "QPushButton#removeItemButton {\n"
            "font-family: 'Calibri';\n"
            "font-size: 12pt;\n"
            "font-weight: bold;\n"
            "}\n"
            "\n" + button_style
        )
        self.horizontalLayout.addWidget(self.removeItemButton)

        self.clearCartButton = QPushButton(CartDialog)
        self.clearCartButton.setObjectName("clearCartButton")
        self.clearCartButton.setStyleSheet(
            "QPushButton#clearCartButton {\n"
            "font-family: 'Calibri';\n"
            "font-size: 12pt;\n"
            "font-weight: bold;\n"
            "}\n"
            "\n" + button_style
        )
        self.horizontalLayout.addWidget(self.clearCartButton)

        self.checkoutButton = QPushButton(CartDialog)
        self.checkoutButton.setObjectName("checkoutButton")
        self.checkoutButton.setStyleSheet(
            "QPushButton#checkoutButton {\n"
            "font-family: 'Calibri';\n"
            "font-size: 12pt;\n"
            "font-weight: bold;\n"
            "}\n"
            "\n" + button_style
        )
        self.horizontalLayout.addWidget(self.checkoutButton)

        self.backButton = QPushButton(CartDialog)
        self.backButton.setObjectName("backButton")
        self.backButton.setStyleSheet(
            "QPushButton#backButton {\n"
            "font-family: 'Calibri';\n"
            "font-size: 12pt;\n"
            "font-weight: bold;\n"
            "}\n"
            "\n" + button_style
        )
        self.horizontalLayout.addWidget(self.backButton)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(CartDialog)
        QMetaObject.connectSlotsByName(CartDialog)

    def retranslateUi(self, CartDialog):
        CartDialog.setWindowTitle(QCoreApplication.translate("CartDialog", "Form", None))
        self.logoLabel.setText("")
        self.titleLabel.setText(
            QCoreApplication.translate("CartDialog", "Корзина и оформление заказа", None)
        )
        self.totalPriceLabel.setText(
            QCoreApplication.translate("CartDialog", "Итого к оплате: 0.00 руб.", None)
        )
        self.removeItemButton.setText(
            QCoreApplication.translate("CartDialog", "Удалить из корзины", None)
        )
        self.clearCartButton.setText(
            QCoreApplication.translate("CartDialog", "Очистить", None)
        )
        self.checkoutButton.setText(
            QCoreApplication.translate("CartDialog", "Подтвердить заказ", None)
        )
        self.backButton.setText(
            QCoreApplication.translate("CartDialog", "Назад в каталог", None)
        )