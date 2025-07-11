from Voting_System.base.base import *


class LoginWindow(QWidget):
    FIXED_WIDTH = 600
    FIXED_HEIGHT = 400

    BUTTON_TITLE_ADMIN_LOGIN     = "Admin Login"
    BUTTON_TITLE_VOTER_LOGIN     = "Voter Login"
    BUTTON_TTILE_CANDIDATE_LOGIN = "Candidate Login"

    def __init__(self):
        super().__init__()
        self.setWindowTitle(TITLE_LOGIN_PAGE)
        self.setWindowIcon( ovs_app_config.getIcon() )
        self.setStyleSheet(f"background-color: {COLOR_CODE_BACKGROUND};")
        self.setFixedSize(self.FIXED_WIDTH, self.FIXED_HEIGHT)
        self.center_window()

        self.setup_ui()

    def center_window(self):
        screen = self.screen().availableGeometry()
        x = (screen.width() - self.FIXED_WIDTH) // 2
        y = (screen.height() - self.FIXED_HEIGHT) // 2
        self.setGeometry(QRect(x, y, self.FIXED_WIDTH, self.FIXED_HEIGHT))

    def setup_ui(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        heading = QLabel(TITLE_LOGIN_PAGE)
        heading.setAlignment(Qt.AlignCenter)
        heading.setFont( ovs_app_config.getHeadingFont() )
        heading.setStyleSheet(CSS_STYLE_FOR_TOP_HEADING)
        layout.addWidget(heading)

        layout.addSpacing(40)


        btn_admin = QPushButton(LoginWindow.BUTTON_TITLE_ADMIN_LOGIN)
        btn_admin.setStyleSheet(CSS_STYLE_FOR_BUTTONS)

        btn_candidate = QPushButton(LoginWindow.BUTTON_TTILE_CANDIDATE_LOGIN)
        btn_candidate.setStyleSheet(CSS_STYLE_FOR_BUTTONS)

        btn_voter = QPushButton(LoginWindow.BUTTON_TITLE_VOTER_LOGIN)
        btn_voter.setStyleSheet(CSS_STYLE_FOR_BUTTONS)

        layout.addWidget(btn_admin)
        layout.addSpacing(15)
        layout.addWidget(btn_candidate)
        layout.addSpacing(15)
        layout.addWidget(btn_voter)

        self.setLayout(layout)
