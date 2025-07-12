from Voting_System.base.base import *
from .admin_login import *
from .candidate_login import *
from .voter_login import *

class LoginWindow(QWidget):
    FIXED_WIDTH = 600
    FIXED_HEIGHT = 400

    def __init__(self):
        super().__init__()
        self.setWindowTitle(TITLE_LOGIN_PAGE)
        self.setWindowIcon( ovs_app_config.getIcon() )
        self.setStyleSheet( CSS_STYLE_FOR_WIDGETS )
        self.setFixedSize(self.FIXED_WIDTH, self.FIXED_HEIGHT)
        self.center_window()

        self.admin_login = AdminLogin()
        self.candidate_login = CandidateLogin()
        self.voter_login = VoterLogin()

        self.setup_ui()

    def center_window(self):
        screen = ovs_app_config.getScreen()
        x = (screen.width() - self.FIXED_WIDTH) // 2
        y = (screen.height() - self.FIXED_HEIGHT) // 2
        self.setGeometry(QRect(x, y, self.FIXED_WIDTH, self.FIXED_HEIGHT))

    def setup_ui(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget( ovs_app_config.createHeading( TITLE_LOGIN_PAGE) )

        layout.addSpacing(40)

        btn_admin = QPushButton(TITLE_ADMIN_LOGIN_PAGE)
        btn_admin.setStyleSheet(CSS_STYLE_FOR_BUTTONS)
        btn_admin.clicked.connect( self.admin_login.show )

        btn_candidate = QPushButton(TTILE_CANDIDATE_LOGIN_PAGE)
        btn_candidate.setStyleSheet(CSS_STYLE_FOR_BUTTONS)
        btn_candidate.clicked.connect( self.candidate_login.show )

        btn_voter = QPushButton(TITLE_VOTER_LOGIN_PAGE)
        btn_voter.setStyleSheet(CSS_STYLE_FOR_BUTTONS)
        btn_voter.clicked.connect( self.voter_login.show )

        layout.addWidget(btn_admin)
        layout.addSpacing(15)
        layout.addWidget(btn_candidate)
        layout.addSpacing(15)
        layout.addWidget(btn_voter)

        self.setLayout(layout)
    
    def closeEvent(self , event : QCloseEvent) -> None:
        self.admin_login.close()
        self.voter_login.close()
        self.candidate_login.close()

        event.accept
