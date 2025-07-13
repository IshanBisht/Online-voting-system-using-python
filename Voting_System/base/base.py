from .data_manager import *

PATH_TO_MAIN_PAGE_BACKGROUND_IMAGE = "Images/background.jpg"
PATH_TO_APP_ICON                   = "Images/icon.png"
COLOR_CODE_BACKGROUND              = "#567DD0"
TITLE_MAIN_PAGE                    = "Online Voting System"

TITLE_REGISTRATION_PAGE            = "Register to OVS"
TITLE_CANDIDATE_REGISTRATION_PAGE  = "Candidate Registration"
TITLE_VOTER_REGISTRATION_PAGE      = "Voter Registration"

TITLE_LOGIN_PAGE                   = "Login to OVS"
TITLE_ADMIN_LOGIN_PAGE             = "Admin Login"
TITLE_VOTER_LOGIN_PAGE             = "Voter Login"
TTILE_CANDIDATE_LOGIN_PAGE         = "Candidate Login"

CSS_STYLE_FOR_BUTTONS = """
    QPushButton {
        background-color: #ffffff;
        color: #567DD0;
        border-radius: 10px;
        font-size: 16px;
        font-weight: bold;
        padding: 10px 20px;
    }
    QPushButton:hover {
        background-color: #e8e8e8;
    }
"""

CSS_STYLE_FOR_FORM_BUTTONS = """
    QPushButton {
        background-color: #ffffff;
        color: #567DD0;
        border-radius: 8px;
        font-size: 16px;
        font-weight: bold;
        padding: 12px 20px;
    }
    QPushButton:hover {
        background-color: #e0e0e0;
    }
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



    def createHeading( self, title : str ) -> QLabel :
        heading = QLabel( title )
        heading.setAlignment(Qt.AlignmentFlag.AlignCenter)
        heading.setFont( self.getHeadingFont() )
        heading.setStyleSheet( CSS_STYLE_FOR_TOP_HEADING )
        return heading



    def getIcon( self ) -> QIcon : return self.icon



    def getHeadingFont( self ) -> QFont : return self.heading_font



    def getButtonFont( self ) -> QFont  : return self.button_font



    def getScreen( self ) -> QSize : return self.screen


# Global object to cache fonts, icon and other objects for faster loading with low memory usage
ovs_app_config = AppConfigs()