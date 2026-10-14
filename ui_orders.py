# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'orders.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QSize, QMetaObject
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import (
    QAbstractItemView, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
)


class Ui_OrdersDialog(object):
    """Интерфейс окна управления заказами."""

    def setupUi(self, OrdersDialog):
        if not OrdersDialog.objectName():
            OrdersDialog.setObjectName("OrdersDialog")
        OrdersDialog.resize(800, 600)
        OrdersDialog.setMinimumSize(QSize(800, 600))

        window_icon = QIcon()
        window_icon.addFile(
            "images/Чудо Обувь.png",
            QSize(), QIcon.Normal, QIcon.Off
        )
        OrdersDialog.setWindowIcon(window_icon)

        self.verticalLayout = QVBoxLayout(OrdersDialog)
        self.verticalLayout.setObjectName("verticalLayout")

        # ---------- Верхняя панель: заголовок и логотип ----------
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.titleLabel = QLabel(OrdersDialog)
        self.titleLabel.setObjectName("titleLabel")
        self.titleLabel.setStyleSheet(
            "QLabel#titleLabel {\n"
            "font-family: 'Calibri';\n"
            "font-size: 18pt;\n"
            "font-weight: bold;\n"
            "color: #70B2AF;\n"
            "}\n"
        )
        self.horizontalLayout_3.addWidget(self.titleLabel)

        self.horizontalSpacer = QSpacerItem(
            188, 20,
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.label = QLabel(OrdersDialog)
        self.label.setObjectName("label")
        self.label.setMinimumSize(QSize(60, 60))
        self.label.setMaximumSize(QSize(60, 60))
        self.label.setPixmap(QPixmap("images/Чудо Обувь.png"))
        self.label.setScaledContents(True)
        self.horizontalLayout_3.addWidget(self.label)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        # ---------- Подпись над таблицей состава заказа ----------
        self.detailsLabel = QLabel(OrdersDialog)
        self.detailsLabel.setObjectName("detailsLabel")
        self.detailsLabel.setStyleSheet(
            "QLabel#detailsLabel {\n"
            "font-family: 'Calibri';\n"
            "font-size: 16pt;\n"
            "font-weight: bold;\n"
            "color: #70B2AF;\n"
            "}\n"
        )
        self.verticalLayout.addWidget(self.detailsLabel)

        # ---------- Таблица списка заказов ----------
        self.ordersTable = QTableWidget(OrdersDialog)
        self.ordersTable.setObjectName("ordersTable")
        self.ordersTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ordersTable.verticalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.ordersTable)

        # ---------- Таблица состава выбранного заказа ----------
        self.orderDetailsTable = QTableWidget(OrdersDialog)
        self.orderDetailsTable.setObjectName("orderDetailsTable")
        self.verticalLayout.addWidget(self.orderDetailsTable)

        # ---------- Кнопки управления ----------
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        primary_style = (
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

        secondary_style = (
            "QPushButton {\n"
            "background-color: #D2F6E7;\n"
            "color: #333333;\n"
            "border: 1px solid #70B2AF;\n"
            "border-radius: 6px;\n"
            "font-family: 'Calibri';\n"
            "font-size: 12pt;\n"
            "font-weight: bold;\n"
            "}\n"
            "\n"
            "QPushButton#editOrderButton:hover {\n"
            "background-color: #BBEBD7;\n"
            "}"
        )

        self.deleteOrderButton = QPushButton(OrdersDialog)
        self.deleteOrderButton.setObjectName("deleteOrderButton")
        self.deleteOrderButton.setStyleSheet(primary_style)
        self.horizontalLayout.addWidget(self.deleteOrderButton)

        self.editOrderButton = QPushButton(OrdersDialog)
        self.editOrderButton.setObjectName("editOrderButton")
        self.editOrderButton.setStyleSheet(secondary_style)
        self.horizontalLayout.addWidget(self.editOrderButton)

        self.backButton = QPushButton(OrdersDialog)
        self.backButton.setObjectName("backButton")
        self.backButton.setStyleSheet(primary_style)
        self.horizontalLayout.addWidget(self.backButton)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(OrdersDialog)
        QMetaObject.connectSlotsByName(OrdersDialog)

    def retranslateUi(self, OrdersDialog):
        self.titleLabel.setText(
            QCoreApplication.translate("OrdersDialog", "Управление заказами", None)
        )
        self.label.setText("")
        self.detailsLabel.setText(
            QCoreApplication.translate("OrdersDialog", "Состав выбранного заказа:", None)
        )
        self.deleteOrderButton.setText(
            QCoreApplication.translate("OrdersDialog", "Удалить заказ", None)
        )
        self.editOrderButton.setText(
            QCoreApplication.translate("OrdersDialog", "Редактировать заказ", None)
        )
        self.backButton.setText(
            QCoreApplication.translate("OrdersDialog", "Назад", None)
        )
