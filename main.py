from Voting_System.voting import *

if __name__ == "__main__":

    voting_app = QApplication(argv)

    ovs_app_config.prepare()

    main_widget = MainApp( )

    main_widget.show()

    exit( voting_app.exec() )