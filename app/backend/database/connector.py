from mysql.connector import connect

from typing import Tuple, List, Optional


class SummaryDBConnector:
    def __init__(self,
                 # see docker-compose.yml
                 user='root',
                 password='root',
                 host='mysql-db',
                 port='3306'):
        config = {
            'user': user,
            'password': password,
            'host': host,
            'port': port,
            'database': 'summary'
        }
        self._connector = connect(**config)
        self.db = self._connector.cursor()

        self._table_name = "text_data"

    def insert(self, text: str, text_summary: str) -> int:
        """Inserts text data into DB and returns Primary Key ID"""
        insert_cmd = self._insert_cmd(text, text_summary)
        self.db.execute(insert_cmd)

        self._connector.commit()  # commit insert

        return self.db.lastrowid

    def batch_insert(self, insert: List[Tuple[str, str]]):
        raise NotImplementedError

    def query(self, text_id: int) -> List[Optional[Tuple[str, str]]]:
        """
        Query based on Primary Key.

        Returns and empty list if no matching results is found.
        """

        query_cmd = self._query_cmd(text_id=text_id)
        self.db.execute(query_cmd)
        results = self.db.fetchall()  # query
        return results

    def select_all(self):
        cmd = f'SELECT * FROM {self._table_name}'
        self.db.execute(cmd)
        return self.db.fetchall()

    def close(self):
        self._connector.close()

    def _insert_cmd(self, text, text_summary) -> str:
        return f"INSERT INTO {self._table_name}(text, text_summary) VALUES ('{text}', '{text_summary}')"

    def _query_cmd(self, text_id: int) -> str:
        return f'SELECT text, text_summary FROM {self._table_name} WHERE id={text_id}'
