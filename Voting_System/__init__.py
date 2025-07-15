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

        self.registration_window = RegistrationWindow()
        self.login_window = LoginWindow()

        self.setup_ui()



    def center_window(self):
        screen = ovs_app_config.getScreen()
        x = (screen.width() - self.FIXED_WIDTH) // 2
        y = (screen.height() - self.FIXED_HEIGHT) // 2
        self.setGeometry(QRect(x, y, self.FIXED_WIDTH, self.FIXED_HEIGHT))



    def setup_ui(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addLayout( ovs_app_config.createHeading( TITLE_MAIN_PAGE ) )

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
        btn_registration.clicked.connect( self.registration_window.show)

        btn_login = QPushButton("Login")
        btn_login.setStyleSheet(btn_style)
        btn_login.clicked.connect( self.login_window.show )

        layout.addWidget(btn_registration)
        layout.addSpacing(20)
        layout.addWidget(btn_login)

        self.setLayout(layout)
    


    def closeEvent(self , event : QCloseEvent) -> None:
        self.registration_window.close()
        self.login_window.close()
        event.accept()