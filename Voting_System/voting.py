from .Registration.registration import *
from .Login.login import *

class MainApp(QWidget):
    FIXED_WIDTH = 600
    FIXED_HEIGHT = 400

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Online Voting System")
        self.setWindowIcon( ovs_app_config.getIcon() )
        self.setStyleSheet( CSS_STYLE_FOR_WIDGETS )
        self.setFixedSize(self.FIXED_WIDTH, self.FIXED_HEIGHT)
        self.center_window()

        self.registration_window = None
        self.login_window = None

        self.setup_ui()

    def center_window(self):
        screen = ovs_app_config.getScreen()
        x = (screen.width() - self.FIXED_WIDTH) // 2
        y = (screen.height() - self.FIXED_HEIGHT) // 2
        self.setGeometry(QRect(x, y, self.FIXED_WIDTH, self.FIXED_HEIGHT))

    def setup_ui(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        heading = QLabel("Online Voting System")
        heading.setAlignment(Qt.AlignmentFlag.AlignCenter)
        heading.setFont( ovs_app_config.getHeadingFont() )
        heading.setStyleSheet("color: white;")
        layout.addWidget(heading)

        layout.addSpacing(40)

        btn_style = """
            QPushButton {
                background-color: #ffffff;
                color: #567DD0;
                border-radius: 10px;
                font-size: 18px;
                font-weight: bold;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #f0f0f0;
            }
        """

        btn_registration = QPushButton("Registration")
        btn_registration.setStyleSheet(btn_style)
        btn_registration.clicked.connect(self.open_registration)

        btn_login = QPushButton("Login")
        btn_login.setStyleSheet(btn_style)
        btn_login.clicked.connect(self.open_login)

        layout.addWidget(btn_registration)
        layout.addSpacing(20)
        layout.addWidget(btn_login)

        self.setLayout(layout)

    def open_registration(self):
        self.registration_window = RegistrationWindow()
        self.registration_window.show()

    def open_login(self):
        self.login_window = LoginWindow()
        self.login_window.show()
