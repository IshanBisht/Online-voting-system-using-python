from .imports import *

PATH_TO_MAIN_PAGE_BACKGROUND_IMAGE = "Images/background.jpg"
PATH_TO_APP_ICON                   = "Images/icon.png"
COLOR_CODE_BACKGROUND              = "#567DD0"
TITLE_MAIN_PAGE                    = "Online Voting System"
TITLE_LOGIN_PAGE                   = "Login to OVS"
TITLE_REGISTRATION_PAGE            = "Register to OVS"

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

CSS_STYLE_FOR_TOP_HEADING = """
    color: white;
"""


class AppConfigs :

    def __init__( self ) :  
        self.icon = None
        self.heading_font = None
        self.button_font = None


    
    def prepare( self ) -> None :
        self.icon = QIcon( PATH_TO_APP_ICON )
        self.heading_font = QFont("Arial", 22, QFont.Bold)
        self.button_font = QFont("Arial", 22, QFont.Bold)



    def getIcon( self ) -> QIcon : return self.icon



    def getHeadingFont( self ) -> QFont : return self.heading_font



    def getButtonFont( self ) -> QFont  : return self.button_font


# Global object to cache fonts, icon and other objects for faster loading with low memory usage
ovs_app_config = AppConfigs()