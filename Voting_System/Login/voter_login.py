from Voting_System.base.base import *


class VoterLogin(QWidget):
    FIXED_WIDTH = 500
    FIXED_HEIGHT = 500

    def __init__(self):
        super().__init__()

        self.setWindowTitle( TITLE_VOTER_LOGIN_PAGE )
        self.setWindowIcon( ovs_app_config.getIcon() )
        self.setStyleSheet( CSS_STYLE_FOR_WIDGETS )

        self.setFixedSize(self.FIXED_WIDTH, self.FIXED_HEIGHT)
        self.setup_ui()



    def setup_ui(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.setContentsMargins(30, 20, 30, 20)
        layout.setSpacing(20)

        layout.addLayout( ovs_app_config.createHeading( TITLE_VOTER_LOGIN_PAGE ) )

        form_layout = QVBoxLayout()
        form_layout.setSpacing(18)

        # Voter ID
        self.voter_id = QLineEdit()
        self.voter_id.setValidator( ovs_app_config.getUnsignedIntValidator() )
        self.voter_id.setPlaceholderText("Enter Voter ID")
        form_layout.addWidget(self._labeled_widget("Voter ID", self.voter_id, CSS_STYLE_FOR_INPUT_LABELS ))

        # Password
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        self.password.setPlaceholderText("Enter Password")
        form_layout.addWidget(self._labeled_widget("Password", self.password, CSS_STYLE_FOR_INPUT_LABELS ))

        # Login Button
        login_btn = QPushButton("Login")
        login_btn.setStyleSheet( CSS_STYLE_FOR_FORM_BUTTONS )
        login_btn.clicked.connect(self.validate_login)
        form_layout.addSpacing(30)
        form_layout.addWidget(login_btn)

        create_account_btn = QPushButton("REGISTER A NEW VOTER ACCOUNT")
        create_account_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: white;
                font-size: 14px;
                font-weight: bold;
                text-decoration: underline;
                border: none;
            }
            QPushButton:hover {
                color: #d0dfff;
            }
        """)
        create_account_btn.clicked.connect(self.create_account_clicked)
        form_layout.addWidget(create_account_btn)

        form_widget = QWidget()
        form_widget.setLayout(form_layout)
        form_widget.setStyleSheet( CSS_STYLE_FOR_INPUT_BOX )

        layout.addWidget(form_widget)
        self.setLayout(layout)

    def _labeled_widget(self, label_text, widget, label_style):
        container = QVBoxLayout()
        label = QLabel(label_text)
        label.setStyleSheet(label_style)
        container.addWidget(label)
        container.addWidget(widget)
        box = QWidget()
        box.setLayout(container)
        return box

    def validate_login(self):
        voter_id = self.voter_id.text().strip()
        password = self.password.text().strip()

        if not voter_id or not password:
            QMessageBox.warning(self, "Incomplete", "Please enter both Voter ID and Password.")
            return

        # Placeholder success message
        QMessageBox.information(self, "Login Successful", f"Welcome, {voter_id}!")

    def create_account_clicked(self): pass
        # QMessageBox.information(self, "Redirect", "Redirecting to Voter Registration Page...")

