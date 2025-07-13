class OvsWrongLoginInfoException ( Exception ):

    def __str__(self) : return "You have entered the wrong ID and Password!"

class OvsInvalidCandidateIDException ( Exception ) :

    def __str__(self) : return "You have entered the invalid candidate ID!"

class OvsInvalidAdminIDException ( Exception ) :

    def __str__(self) : return "You have entered the invalid Admin ID!"

class OvsInvalidVoterIDException ( Exception ) :

    def __str__(self) : return "You have entered the invalid Voter ID!"