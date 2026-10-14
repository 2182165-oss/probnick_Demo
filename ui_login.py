# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QRect, QMetaObject
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtWidgets import (
    QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QStatusBar, QWidget
)


class Ui_MainWindow(object):
    """Интерфейс окна авторизации."""

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1470, 653)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Заголовок окна
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(620, 10, 201, 20))
        title_font = QFont()
        title_font.setPointSize(18)
        self.label.setFont(title_font)

        # Логотип компании
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(QRect(1230, 0, 241, 151))
        self.label_2.setPixmap(QPixmap(
            "programming_course-main/Прил_2_ОЗ_КИМ_09.02.07-2-2027/Images/Чудо Обувь.png"
        ))
        self.label_2.setScaledContents(True)

        # Поле ввода логина
        self.loginLineEdit = QLineEdit(self.centralwidget)
        self.loginLineEdit.setObjectName("loginLineEdit")
        self.loginLineEdit.setGeometry(QRect(540, 520, 361, 51))

        # Кнопки
        self.loginButton = QPushButton(self.centralwidget)
        self.loginButton.setObjectName("loginButton")
        self.loginButton.setGeometry(QRect(570, 530, 111, 31))

        self.guestButton = QPushButton(self.centralwidget)
        self.guestButton.setObjectName("guestButton")
        self.guestButton.setGeometry(QRect(760, 530, 111, 31))

        MainWindow.setCentralWidget(self.centralwidget)

        # Строка меню
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 1470, 19))
        MainWindow.setMenuBar(self.menubar)

        # Строка состояния
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", "Вход в систему", None))
        self.label_2.setText("")
        self.loginButton.setText(QCoreApplication.translate("MainWindow", "Войти", None))
        self.guestButton.setText(QCoreApplication.translate("MainWindow", "Вход для гостя", None))