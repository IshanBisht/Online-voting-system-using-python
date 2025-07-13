from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QComboBox, QCheckBox
from PyQt5.QtGui import QIcon, QFont , QPixmap, QPalette, QBrush, QCloseEvent, QIntValidator
from PyQt5.QtCore import Qt, QRect, QSize, QCoreApplication, QSize

from sys import argv , exit
from hashlib import sha256
import mysql.connector