# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'autorazation.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QRect, QSize, QMetaObject
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QComboBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget
)


class Ui_MainWindow(object):
    """Интерфейс главного окна — каталог товаров."""

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(811, 608)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        # ---------- Верхняя панель: логотип, заголовок, инфо пользователя, выход ----------
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.logoLabel = QLabel(self.centralwidget)
        self.logoLabel.setObjectName("logoLabel")
        self.logoLabel.setMaximumSize(QSize(64, 64))
        self.logoLabel.setPixmap(QPixmap(
            "../Рабочий стол/Images/Чудо Обувь.ico"
        ))
        self.logoLabel.setScaledContents(True)
        self.horizontalLayout.addWidget(self.logoLabel)

        self.titleLabel = QLabel(self.centralwidget)
        self.titleLabel.setObjectName("titleLabel")
        self.titleLabel.setStyleSheet(
            "QLabel#titleLabel {\n"
            "font-family: 'Calibri';\n"
            "font-size: 18pt;\n"
            "font-weight: bold;\n"
            "color: #70B2AF;\n"
            "}\n"
        )
        self.horizontalLayout.addWidget(self.titleLabel)

        self.horizontalSpacer = QSpacerItem(
            40, 20,
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.userinfolabel = QLabel(self.centralwidget)
        self.userinfolabel.setObjectName("userinfolabel")
        self.userinfolabel.setStyleSheet(
            "QLabel#userinfolabel {\n"
            "font-family: 'Calibri';\n"
            "font-size: 12pt;\n"
            "font-weight: bold;\n"
            "}"
        )
        self.horizontalLayout.addWidget(self.userinfolabel)

        self.LogoutButton = QPushButton(self.centralwidget)
        self.LogoutButton.setObjectName("LogoutButton")
        self.LogoutButton.setStyleSheet(
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
            "}"
        )
        self.horizontalLayout.addWidget(self.LogoutButton)

        self.verticalLayout.addLayout(self.horizontalLayout)

        # ---------- Панель поиска, фильтрации и сортировки ----------
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.searchLineEdit = QLineEdit(self.centralwidget)
        self.searchLineEdit.setObjectName("searchLineEdit")
        self.searchLineEdit.setStyleSheet(
            "QLineEdit#searchLineEdit {\n"
            "font-family: 'Calibri';\n"
            "font-size: 12pt;\n"
            "font-weight: bold;\n"
            "}"
        )
        self.horizontalLayout_2.addWidget(self.searchLineEdit)

        self.filterComboBox = QComboBox(self.centralwidget)
        self.filterComboBox.setObjectName("filterComboBox")
        self.filterComboBox.setStyleSheet(
            "QComboBox#filterComboBox {\n"
            "font-family: 'Calibri';\n"
            "font-size: 12pt;\n"
            "font-weight: bold;\n"
            "background-color: #70B2AF\n"
            "}"
        )
        self.horizontalLayout_2.addWidget(self.filterComboBox)

        self.sortComboBox = QComboBox(self.centralwidget)
        self.sortComboBox.setObjectName("sortComboBox")
        self.sortComboBox.setStyleSheet(
            "QComboBox#sortComboBox {\n"
            "font-family: 'Calibri';\n"
            "font-size: 12pt;\n"
            "font-weight: bold;\n"
            "background-color: #70B2AF\n"
            "}"
        )
        self.horizontalLayout_2.addWidget(self.sortComboBox)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        # ---------- Таблица товаров ----------
        self.productsTable = QTableWidget(self.centralwidget)
        self.productsTable.setObjectName("productsTable")
        self.verticalLayout.addWidget(self.productsTable)

        # ---------- Нижняя панель: кнопки действий ----------
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.horizontalSpacer_2 = QSpacerItem(
            358, 20,
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.addToOrderButton = QPushButton(self.centralwidget)
        self.addToOrderButton.setObjectName("addToOrderButton")
        self.addToOrderButton.setStyleSheet(
            "QPushButton#addToOrderButton {\n"
            "font-family: 'Calibri';\n"
            "font-size: 12pt;\n"
            "font-weight: bold;\n"
            "}\n"
            "\n"
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
        self.horizontalLayout_3.addWidget(self.addToOrderButton)

        self.manageOrdersButton = QPushButton(self.centralwidget)
        self.manageOrdersButton.setObjectName("manageOrdersButton")
        self.manageOrdersButton.setStyleSheet(
            "QPushButton#manageOrdersButton {\n"
            "font-family: 'Calibri';\n"
            "font-size: 12pt;\n"
            "font-weight: bold;\n"
            "}\n"
            "\n"
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
        self.horizontalLayout_3.addWidget(self.manageOrdersButton)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)

        # ---------- Строка меню ----------
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 811, 19))
        MainWindow.setMenuBar(self.menubar)

        # ---------- Строка состояния ----------
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "MainWindow", None))
        self.logoLabel.setText("")
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", "Каталог товаров", None))
        self.userinfolabel.setText(QCoreApplication.translate("MainWindow", "TextLabel", None))
        self.LogoutButton.setText(QCoreApplication.translate("MainWindow", "Выйти", None))
        self.searchLineEdit.setText("")
        self.searchLineEdit.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Введите название для поиска", None)
        )
        self.addToOrderButton.setText(
            QCoreApplication.translate("MainWindow", "Добавить заказ/Корзина", None)
        )
        self.manageOrdersButton.setText(
            QCoreApplication.translate("MainWindow", "Управление заказами", None)
        )