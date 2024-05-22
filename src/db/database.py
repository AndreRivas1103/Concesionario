
import sqlite3
from typing import Optional
import datetime

from src.exceptions import db_exceptions
from src.models.user import User


class Database:
    __DATABASE_URL = "src/db/app.db"

    _con: Optional[sqlite3.Connection] = None
    _cur: Optional[sqlite3.Cursor] = None

    @staticmethod
    def _connect():

        Database._con = sqlite3.connect(Database.__DATABASE_URL)
        Database._cur = Database._con.cursor()

    @staticmethod
    def _disconnect():

        if Database._cur:
            Database._cur.close()
        if Database._con:
            Database._con.close()

    @staticmethod
    def add_user(name: str, phone_number: int) -> None:

        Database._connect()
        try:
            query = "SELECT name FROM users WHERE phone_number = :phone_number"
            Database._cur.execute(query, {"phone_number": phone_number})
            result: list[tuple[str]] = Database._cur.fetchall()

            if result:
                raise db_exceptions.PhoneNumberRepeated

            query: str = "INSERT INTO users(name, phone_number) VALUES(:name, :phone_number)"
            Database._cur.execute(query, {"name": name, "phone_number": phone_number})
            Database._con.commit()
        finally:
            Database._disconnect()

    @staticmethod
    def get_user(phone_number: int, name: Optional[str] = None) -> User:
        """method docstring"""
        try:
            Database._connect()
            query: str = str()
            if name:
                query = "SELECT id, name, phone_number FROM users WHERE phone_number = :phone_number AND name = :name"
            else:
                query = "SELECT id, name, phone_number FROM users WHERE phone_number = :phone_number"
            Database._cur.execute(query, {"phone_number": phone_number, "name": name})
            result_query: list[tuple[int, str]] = Database._cur.fetchall()
            if not result_query:
                raise db_exceptions.PhoneNumberRepeated
            result: User = User(number_id = result_query[0][0],
                            name = result_query[0][1],
                            phone_number=result_query[0][2])
            return result
        finally:
            Database._disconnect()

    @staticmethod
    def user_exist(name: str, phone_number: int) -> bool:
        """method docstring"""
        try:
            Database._connect()
            query: str = "SELECT * FROM users WHERE phone_number = :phone_number AND name = :name"
            Database._cur.execute(query, {"phone_number": phone_number, "name": name})
            result: list[tuple[int, str, int]] = Database._cur.fetchall()
            if result:
                return True
            else:
                return False
        finally:
            Database._disconnect()

    @staticmethod
    def get_available_datetime() -> dict[datetime.date, list[datetime.time]]:
        Database._connect()
        try:
            query = "SELECT test_day, test_hour FROM driver_test WHERE available = 1"
            Database._cur.execute(query)
            result_query: list[tuple[str, str]] = Database._cur.fetchall()
            available_datetime: dict[datetime.date, list[datetime.time]] = dict()
            for date_str, hour_str in result_query:
                test_date = datetime.date.fromisoformat(date_str)
                test_hour = datetime.datetime.strptime(hour_str, "%H:%M:%S").time()
                if test_date not in available_datetime:
                    available_datetime[test_date] = list()
                available_datetime[test_date].append(test_hour)
            return available_datetime
        finally:
            Database._disconnect()





if __name__ == '__main__':
    # agregar la lógica para crear la tabla
    pass
