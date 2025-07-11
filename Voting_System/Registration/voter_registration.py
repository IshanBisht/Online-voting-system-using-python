
from Voting_System.base.base import *

class VoterRegistration(QWidget):
    FIXED_WIDTH = 600

    def __init__(self):
        super().__init__()

        self.setWindowTitle( TITLE_VOTER_REGISTRATION_PAGE )
        self.setWindowIcon( ovs_app_config.getIcon() )
        self.setStyleSheet( CSS_STYLE_FOR_WIDGETS )

        self.resize_to_screen()
        self.center_window()
        self.setup_ui()

    def resize_to_screen(self):
        screen = ovs_app_config.getScreen()
        self.FIXED_HEIGHT = int(screen.height() * 0.7)
        self.setFixedSize(self.FIXED_WIDTH, self.FIXED_HEIGHT)

    def center_window(self):
        screen = ovs_app_config.getScreen()
        x = (screen.width() - self.FIXED_WIDTH) // 2
        y = (screen.height() - self.FIXED_HEIGHT) // 2
        self.setGeometry(QRect(x, y, self.FIXED_WIDTH, self.FIXED_HEIGHT))

    def setup_ui(self):
        layout = QVBoxLayout()
        layout.setAlignment( Qt.AlignmentFlag.AlignTop )
        layout.setContentsMargins(30, 20, 30, 20)
        layout.setSpacing(15)

        heading = QLabel("Voter Registration")
        heading.setAlignment( Qt.AlignmentFlag.AlignCenter )
        heading.setFont(QFont("Arial", 24, QFont.Bold))
        heading.setStyleSheet("color: white; margin-bottom: 20px;")
        layout.addWidget(heading)

        form_layout = QVBoxLayout()
        form_layout.setSpacing(18)

        # First Name
        self.first_name = QLineEdit()
        form_layout.addWidget(self._labeled_widget("First Name", self.first_name, CSS_STYLE_FOR_INPUT_LABELS))

        # Last Name
        self.last_name = QLineEdit()
        form_layout.addWidget(self._labeled_widget("Last Name", self.last_name, CSS_STYLE_FOR_INPUT_LABELS))

        # Security Question
        self.security_question = QComboBox()
        self.security_question.addItems([
            "What's your pet name?",
            "Who's your first teacher?",
            "Where's your birthplace?",
            "What's your favorite movie?"
        ])
        form_layout.addWidget(self._labeled_widget("Security Question", self.security_question, CSS_STYLE_FOR_INPUT_LABELS))

        # Security Answer
        self.security_answer = QLineEdit()
        self.security_answer.setPlaceholderText("Write a valid answer of your security question")
        form_layout.addWidget(self._labeled_widget("Answer to Security Question", self.security_answer, CSS_STYLE_FOR_INPUT_LABELS))

        # Aadhar Number
        self.voterid = QLineEdit()
        self.voterid.setMaxLength(10)
        self.voterid.setPlaceholderText("Enter Valid Voter ID")
        form_layout.addWidget(self._labeled_widget("Voter ID", self.voterid, CSS_STYLE_FOR_INPUT_LABELS))

        # Consent Checkbox
        self.agree_checkbox = QCheckBox("All the details I filled are correct and also agree with terms and condition.")
        self.agree_checkbox.setStyleSheet("color: white; font-size: 13px;")
        form_layout.addWidget(self.agree_checkbox)

        # Register Button
        register_btn = QPushButton("Register")
        register_btn.setStyleSheet(CSS_STYLE_FOR_FORM_BUTTONS)
        register_btn.clicked.connect(self.validate_inputs)
        form_layout.addWidget(register_btn)

        form_widget = QWidget()
        form_widget.setLayout(form_layout)
        form_widget.setStyleSheet(CSS_STYLE_FOR_INPUT_BOX)

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

    def validate_inputs(self):
        fname = self.first_name.text().strip()
        lname = self.last_name.text().strip()
        question = self.security_question.currentText()
        answer = self.security_answer.text().strip()
        voter_id = self.voterid.text().strip()
        agreed = self.agree_checkbox.isChecked()

        if not all([fname, lname, question, answer, voter_id]):
            QMessageBox.warning(self, "Incomplete", "Please fill out all fields.")
            return

        if not ( len(voter_id) != 10 or voter_id.isalnum() ):
            QMessageBox.critical(self, "Invalid Aadhar", "Aadhar number must be exactly 12 digits.")
            return

        if not agreed:
            QMessageBox.warning(self, "Agreement Required", "You must agree to the terms and conditions.")
            return

        QMessageBox.information(self, "Success", "Voter registered successfully!")
