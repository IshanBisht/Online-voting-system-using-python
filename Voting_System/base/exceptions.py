class OvsException ( Exception ):
    def __str__(self ) : return "OvsException"

class OvsWrongLoginInfoException ( OvsException ):
    def __str__(self) : return "You have entered the wrong ID and Password!"


class OvsInvalidCandidateIDException ( OvsException ) :
    def __str__(self) : return "You have entered the invalid candidate ID!"


class OvsInvalidAdminIDException ( OvsException ) :
    def __str__(self) : return "You have entered the invalid Admin ID!"


class OvsInvalidVoterIDException ( OvsException ) :
    def __str__(self) : return "You have entered the invalid Voter ID!"


class OvsCandidateAlreadyRegistered( OvsException ) :
    def __str__(self) : return "The candidate is already registered before."


class OvsVoterAlreadyRegistered ( OvsException ) :
    def __str__(self) : return "The voter is already registered before."


class OvsProgrammingError ( OvsException ):
    def __str__(self) : return "Database connection is already closed before but it's methods are being used after closing."

class OvsVoteAlreadyGivenException( OvsException ) :
    def __str__(self) : return "You have already voted before."