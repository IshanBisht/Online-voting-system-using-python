from .imports import *
from .app_variables import *
from .db_variables import *
from .exceptions import *

KEY_FULL_NAME           :int       = 0
KEY_FIRST_NAME          :int       = 1
KEY_LAST_NAME           :int       = 2
KEY_PLACE               :int       = 3
KEY_ID                  :int       = 4
KEY_VOTE_COUNT          :int       = 5
KEY_AADHAR_CARD         :int       = 6


class DataManager:
    
    @staticmethod
    def getHash(__password: str) -> str:
        return sha256(__password.encode()).hexdigest()

    def __init__(self):
        self.conn = mysql.connector.connect(
            host= OVS_HOST,
            user= OVS_USER,
            password= OVS_PASSWORD,
            database= OVS_DATABASE
        )
        self.cursor = self.conn.cursor(dictionary=True)

    def registerCandidate(self, __aadhar_number: int, __first_name: str, __last_name: str, __place: str, __password: str) -> int:
        self.cursor.execute("SELECT id FROM candidates WHERE aadhar = %s", (__aadhar_number,))

        if self.cursor.fetchone():
            raise Exception("Candidate with same Aadhar already exists")

        self.cursor.execute("""
            INSERT INTO candidates (aadhar, first_name, last_name, place, password_hash)
            VALUES (%s, %s, %s, %s, %s)
        """, (__aadhar_number, __first_name, __last_name, __place, self.getHash(__password)))

        self.conn.commit()
        
        return self.cursor.lastrowid + 999

    def getCandidate(self, __candidate_id: int, __password: str) -> dict[int, int | str]:
        id_actual = __candidate_id - 999
        self.cursor.execute("SELECT * FROM candidates WHERE id = %s", (id_actual,))
        row = self.cursor.fetchone()
        if not row:
            raise OvsInvalidCandidateIDException()
        if row['password_hash'] != self.getHash(__password):
            raise OvsWrongLoginInfoException()
        return {
            KEY_FIRST_NAME: row['first_name'],
            KEY_LAST_NAME: row['last_name'],
            KEY_PLACE: row['place'],
            KEY_ID: row['id'] + 999,
            KEY_VOTE_COUNT: row['vote_count'],
            KEY_AADHAR_CARD: row['aadhar']
        }

    def registerVoter(self, __aadhar_number: int, __first_name: str, __last_name: str, __password: str, __place: str) -> int:
        self.cursor.execute("SELECT id FROM voters WHERE aadhar = %s", (__aadhar_number,))
        if self.cursor.fetchone():
            raise Exception("Voter with same Aadhar already exists")

        self.cursor.execute("""
            INSERT INTO voters (aadhar, first_name, last_name, place, password_hash)
            VALUES (%s, %s, %s, %s, %s)
        """, (__aadhar_number, __first_name, __last_name, __place, self.getHash(__password)))
        self.conn.commit()
        return self.cursor.lastrowid + 999

    def getVoter(self, __voter_id: int, __password: str) -> dict[int, int | str]:
        id_actual = __voter_id - 999
        self.cursor.execute("SELECT * FROM voters WHERE id = %s", (id_actual,))
        row = self.cursor.fetchone()
        if not row:
            raise OvsInvalidVoterIDException()
        if row['password_hash'] != self.getHash(__password):
            raise OvsWrongLoginInfoException()
        return {
            KEY_FIRST_NAME: row['first_name'],
            KEY_LAST_NAME: row['last_name'],
            KEY_PLACE: row['place'],
            KEY_ID: row['id'] + 999,
            KEY_AADHAR_CARD: row['aadhar']
        }

    def getAdmin(self, __admin_id: int, __password: str) -> dict[int, int | str]:

        self.cursor.execute(f"SELECT * FROM {OVS_TABLE_ADMIN} WHERE { OVS_COLUMN_ID } = { __admin_id }")
        row = self.cursor.fetchone()
        
        if not row: raise OvsInvalidAdminIDException()
        
        elif row[ OVS_COLUMN_PASSWORD ] != self.getHash(__password): raise OvsWrongLoginInfoException()

        return {
            KEY_FULL_NAME : str(row[ OVS_COLUMN_NAME ]),
            KEY_ID        : int(row[ OVS_COLUMN_ID]),
            KEY_PLACE     : str(row[ OVS_COLUMN_PLACE])
        }

    def addVote(self, __candidate_id: int) -> None:
        id_actual = __candidate_id - 999
        self.cursor.execute("UPDATE candidates SET vote_count = vote_count + 1 WHERE id = %s", (id_actual,))
        self.conn.commit()

    def getWinnerCandidate(self, __place: str) -> dict[int, int | str]:
        self.cursor.execute("""
            SELECT * FROM candidates
            WHERE place = %s
            ORDER BY vote_count DESC
            LIMIT 1
        """, (__place,))
        row = self.cursor.fetchone()
        if not row:
            raise Exception("No candidates found for this place")
        return {
            KEY_FIRST_NAME: row['first_name'],
            KEY_LAST_NAME: row['last_name'],
            KEY_PLACE: row['place'],
            KEY_ID: row['id'] + 999,
            KEY_VOTE_COUNT: row['vote_count'],
            KEY_AADHAR_CARD: row['aadhar']
        }

    def getResult(self, __place: str) -> list[dict[int, int | str]]:
        self.cursor.execute("SELECT * FROM candidates WHERE place = %s ORDER BY vote_count DESC", (__place,))
        rows = self.cursor.fetchall()
        results = []
        for row in rows:
            results.append({
                KEY_FIRST_NAME: row['first_name'],
                KEY_LAST_NAME: row['last_name'],
                KEY_PLACE: row['place'],
                KEY_ID: row['id'] + 999,
                KEY_VOTE_COUNT: row['vote_count'],
                KEY_AADHAR_CARD: row['aadhar']
            })
        return results


ovs_data_manager = DataManager()