from Voting_System.base.base import *

class ElectionResult(QWidget) :

    FIXED_WIDTH = 500
    FIXED_HEIGHT = 600

    def __init__(self) :

        super().__init__()

        self.setWindowIcon( ovs_app_config.getIcon() )
        self.setStyleSheet( CSS_STYLE_FOR_WIDGETS )
        self.setWindowTitle( TITLE_RESULT_DASHBOARD )
        self.setFixedSize( self.FIXED_WIDTH , self.FIXED_HEIGHT )

        layout = QVBoxLayout()

        layout.addLayout( ovs_app_config.createHeading( TITLE_RESULT_DASHBOARD ) )

        refresh_btn = QPushButton("Refresh")
        refresh_btn.setStyleSheet( CSS_STYLE_FOR_BUTTONS )
        refresh_btn.clicked.connect( self.showResults )

        layout.addWidget( refresh_btn )
        

        self.setLayout(layout)

    def showResults( self ) -> None :
        pass
