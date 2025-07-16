from .data_manager import *


CSS_STYLE_FOR_BUTTONS = f"""
    QPushButton {{
        background-color: #ffffff;
        color: {COLOR_CODE_BACKGROUND};
        border-radius: 10px;
        font-size: 16px;
        font-weight: bold;
        padding: 10px 20px;
    }}
    QPushButton:hover {{
        background-color: #e8e8e8;
    }}
"""

CSS_STYLE_FOR_FORM_BUTTONS = f"""
    QPushButton {{
        background-color: #ffffff;
        color: {COLOR_CODE_BACKGROUND};
        border-radius: 8px;
        font-size: 16px;
        font-weight: bold;
        padding: 12px 20px;
    }}
    QPushButton:hover {{
        background-color: #e0e0e0;
    }}
"""

CSS_STYLE_FOR_TOP_HEADING = """
    color: white;
    font-weight:bolder;
"""

CSS_STYLE_FOR_WIDGETS = f"""
    background-color:{COLOR_CODE_BACKGROUND};
    color:white
"""

CSS_STYLE_FOR_INPUT_BOX = """
    QLineEdit, QComboBox {
        min-height: 38px;
        border-radius: 6px;
        border: 1px solid #ccc;
        font-size: 15px;
        font-weight: bold;
        background-color:white;
        color:black
    }
"""

CSS_STYLE_FOR_INPUT_LABELS = """
    color: white;
    font-weight: bold;
    font-size: 14px;
    margin-bottom: 4px;
"""


class AppConfigs :

    def __init__( self ) :  
        self.icon = None
        self.heading_font = None
        self.button_font = None
        self.screen = None



    def prepare( self ) -> None :
        self.icon = QIcon( PATH_TO_APP_ICON )
        self.heading_font = QFont("Arial", 24, QFont.Weight.Bold)
        self.button_font = QFont("Arial", 22, QFont.Weight.Bold)
        self.screen = QApplication.primaryScreen().size()





    def createHeading(self, title: str) -> QHBoxLayout:
        layout = QHBoxLayout()

        # Load and resize election_commission.png
        left_image_label = QLabel()
        left_pixmap = QPixmap(PATH_TO_ELECTION_COMM_IMAGE , "png").scaled(
            100, 60, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation
        )
        left_image_label.setPixmap(left_pixmap)
        left_image_label.setAlignment(Qt.AlignmentFlag.AlignLeft)

        # Load and resize ashok_chakra.png
        right_image_label = QLabel()
        right_pixmap = QPixmap(PATH_TO_ASHOKA_CHAKRA_IMAGE, "png").scaled(
            60, 60, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation
        )
        right_image_label.setPixmap(right_pixmap)
        right_image_label.setAlignment(Qt.AlignmentFlag.AlignRight)

        # Create the heading label
        heading = QLabel(title)
        heading.setAlignment(Qt.AlignmentFlag.AlignCenter)
        heading.setFont(self.getHeadingFont())
        heading.setStyleSheet(CSS_STYLE_FOR_TOP_HEADING)

        # Add to layout with stretches
        layout.addWidget(left_image_label)
        layout.addStretch(1)
        layout.addWidget(heading)
        layout.addStretch(1)
        layout.addWidget(right_image_label)

        return layout



    def getIcon( self ) -> QIcon : return QIcon() if self.icon == None else self.icon



    def getHeadingFont( self ) -> QFont : return self.heading_font



    def getButtonFont( self ) -> QFont  : return self.button_font



    def getScreen( self ) -> QSize : return self.screen



    def getAlphabetValidator( self ) -> QRegularExpressionValidator : return QRegularExpressionValidator(QRegularExpression("^[a-zA-Z]*$"))



    def getUnsignedIntValidator( self ) -> QIntValidator : return QIntValidator(0, 2147483647)
    


# Global object to cache fonts, icon and other objects for faster loading with low memory usage
ovs_app_config = AppConfigs()