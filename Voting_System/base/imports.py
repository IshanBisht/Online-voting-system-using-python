from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QComboBox, QCheckBox, QGridLayout
from PyQt5.QtGui import QIcon, QFont , QPixmap, QPalette, QBrush, QCloseEvent, QIntValidator, QRegularExpressionValidator
from PyQt5.QtCore import Qt, QRect, QSize, QCoreApplication, QSize, QRegularExpression

from sys import argv , exit
from hashlib import sha256
import pymysql
from pymysql.cursors import DictCursor