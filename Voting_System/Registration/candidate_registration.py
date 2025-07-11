from Voting_System.base.base import *

class CandidateRegistration(QWidget):
    FIXED_WIDTH = 600

    def __init__(self):
        super().__init__()

        self.setWindowTitle(TITLE_CANDIDATE_REGISTRATION_PAGE)
        self.setWindowIcon( ovs_app_config.getIcon() )
        self.setStyleSheet(CSS_STYLE_FOR_WIDGETS)

        self.resize_to_screen( )
        self.center_window( )
        self.setup_ui()

    def resize_to_screen( self ) -> None:
        screen = ovs_app_config.getScreen()
        self.FIXED_HEIGHT = int(screen.height() * 0.8)  # use 80% of screen height
        self.setFixedSize(self.FIXED_WIDTH, self.FIXED_HEIGHT)

    def center_window( self ) -> None:
        screen = ovs_app_config.getScreen()
        x = (screen.width() - self.FIXED_WIDTH) // 2
        y = (screen.height() - self.FIXED_HEIGHT) // 2
        self.setGeometry(QRect(x, y, self.FIXED_WIDTH, self.FIXED_HEIGHT))

    def setup_ui(self):
        layout = QVBoxLayout()
        layout.setAlignment( Qt.AlignmentFlag.AlignTop )
        layout.setContentsMargins(30, 20, 30, 20)
        layout.setSpacing(15)

        heading = QLabel(TITLE_CANDIDATE_REGISTRATION_PAGE)
        heading.setAlignment( Qt.AlignmentFlag.AlignCenter )
        heading.setFont( ovs_app_config.getHeadingFont() )
        heading.setStyleSheet( CSS_STYLE_FOR_TOP_HEADING )
        layout.addWidget(heading)

        form_layout = QVBoxLayout()
        form_layout.setSpacing(18)


        # First Name
        self.first_name = QLineEdit()
        form_layout.addWidget(self._labeled_widget("First Name", self.first_name, CSS_STYLE_FOR_INPUT_LABELS))

        # Last Name
        self.last_name = QLineEdit()
        form_layout.addWidget(self._labeled_widget("Last Name", self.last_name, CSS_STYLE_FOR_INPUT_LABELS))

        # Email
        self.email = QLineEdit()
        self.email.setPlaceholderText("Enter a valid email")
        form_layout.addWidget(self._labeled_widget("Email", self.email, CSS_STYLE_FOR_INPUT_LABELS))

        # Security Question
        self.security_question = QComboBox()
        self.security_question.addItems([
            "What's your pet name?",
            "Who's your first teacher?",
            "Where's your birthplace?",
            "What's your favorite movie?"
        ])
        form_layout.addWidget(self._labeled_widget("Security Question", self.security_question, CSS_STYLE_FOR_INPUT_LABELS))

        # Answer to security question
        self.security_answer = QLineEdit()
        self.security_answer.setPlaceholderText("Write a valid answer of your security question")
        form_layout.addWidget(self._labeled_widget("Answer to Security Question", self.security_answer, CSS_STYLE_FOR_INPUT_LABELS))

        # Aadhar Number
        self.aadhar = QLineEdit()
        self.aadhar.setMaxLength(12)
        self.aadhar.setPlaceholderText("Enter 12-digit Aadhar Number")
        form_layout.addWidget(self._labeled_widget("Aadhar Number", self.aadhar, CSS_STYLE_FOR_INPUT_LABELS))

        # Checkbox
        self.agree_checkbox = QCheckBox("All the details filled are correct and I agree with all the terms and conditions.")
        self.agree_checkbox.setStyleSheet("color: white; font-size: 13px;")
        form_layout.addWidget(self.agree_checkbox)

        # Register Button
        register_btn = QPushButton("Register")
        register_btn.setStyleSheet( CSS_STYLE_FOR_FORM_BUTTONS )
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
        email = self.email.text().strip()
        question = self.security_question.currentText()
        answer = self.security_answer.text().strip()
        aadhar = self.aadhar.text().strip()
        agreed = self.agree_checkbox.isChecked()

        if not all([fname, lname, email, question, answer, aadhar]):
            QMessageBox.warning(self, "Incomplete", "Please fill out all fields.")
            return

        if not aadhar.isdigit() or len(aadhar) != 12:
            QMessageBox.critical(self, "Invalid Aadhar", "Aadhar number must be exactly 12 digits.")
            return

        if not agreed:
            QMessageBox.warning(self, "Agreement Required", "You must agree to the terms and conditions.")
            return

        QMessageBox.information(self, "Success", "Candidate registered successfully!")
