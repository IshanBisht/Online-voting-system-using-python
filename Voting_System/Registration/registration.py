from Voting_System.base.base import *


class RegistrationWindow(QWidget):
    FIXED_WIDTH = 600
    FIXED_HEIGHT = 400

    BUTTON_TITLE_CANDIDATE_REGISTRATION = "Candidate Registration"
    BUTTON_TITLE_VOTER_REGISTRATION     = "Voter Registration"

    def __init__(self):
        super().__init__()
        self.setWindowTitle(TITLE_REGISTRATION_PAGE)
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

        heading = QLabel(TITLE_REGISTRATION_PAGE)
        heading.setAlignment(Qt.AlignCenter)
        heading.setFont( ovs_app_config.getHeadingFont() )
        heading.setStyleSheet(CSS_STYLE_FOR_TOP_HEADING)
        layout.addWidget(heading)

        layout.addSpacing(40)

        btn_candidate = QPushButton(RegistrationWindow.BUTTON_TITLE_CANDIDATE_REGISTRATION)
        btn_candidate.setStyleSheet(CSS_STYLE_FOR_BUTTONS)

        btn_voter = QPushButton(RegistrationWindow.BUTTON_TITLE_VOTER_REGISTRATION)
        btn_voter.setStyleSheet(CSS_STYLE_FOR_BUTTONS)

        layout.addWidget(btn_candidate)
        layout.addSpacing(20)
        layout.addWidget(btn_voter)

        self.setLayout(layout)
