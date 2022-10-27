import pymysql
from pymysql.cursors import DictCursor
from typing import Tuple, Union, List, Dict

from led_control.utils import LoggingClass


class DB(LoggingClass):
    def __init__(self):
        """
        > cat  ~/.my.cnf
        [client]
        host=szerviz.weloveapple.hu
        user=weloveapple
        password=alma
        databas=weloveapple
        """
        super().__init__()
        self.dbconn = pymysql.connect(
            read_default_file="~/.my.cnf",
            connect_timeout=10,
            read_timeout=10,
            write_timeout=10,
            charset="utf8",
            use_unicode=True,
            cursorclass=DictCursor,
        )

    def sql(self, sql: str, args: Union[Tuple, List, Dict] = None) -> Tuple:
        with self.dbconn.cursor() as cursor:
            try:
                cursor.execute(sql, args)
            except pymysql.ProgrammingError as e:
                self.logger.warning(
                    f"Failed to query DB due to {e}\n call was: {sql} with args: {args}",
                    exc_info=True,
                )
            else:
                self.dbconn.commit()
                return cursor.fetchall()
            return ()
