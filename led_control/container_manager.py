from led_control.database import DB
from led_control.datastore import contaiener_data, DBFields, DB_TABLE
from led_control.led_controller import LEDControl
from led_control.utils import LoggingClass


class Container(LoggingClass):
    def __init__(self):
        super().__init__()
        self.db = DB()
        self.led_control = LEDControl()
        self.last_update = None

    def init_leds(self):
        """
        Iterate through all containers, select the latest status and set the LED accordingly
        """
        _sql = f"SELECT work_state_id as id FROM worksheets WHERE container = %s ORDER BY updated_at DESC LIMIT 1"
        for container in contaiener_data.keys():
            _query_result = self.db.sql(sql=_sql, args=[container])
            if len(_query_result) and _query_result[0].get(DBFields.id):
                self.led_control.set_status(
                    container=container, status_id=_query_result[0].get(DBFields.id)
                )

    def query_and_update_states(self):
        if not self.last_update:
            _results_after = "NOW() - INTERVAL 30 DAY"
        else:
            _results_after = self.last_update
        _sql = (
            f"SELECT {DBFields.container},{DBFields.id},{DBFields.updated_at} "
            f"FROM {DB_TABLE} "
            f"WHERE {DBFields.updated_at} >= %s "
            f"ORDER BY {DBFields.updated_at} "
            f"DESC LIMIT 1"
        )
        _query_results = self.db.sql(sql=_sql, args=[_results_after])
        self.logger.info(f"Updating {len(_query_results)} container status(es)")
        for query_result in _query_results:
            self.led_control.set_status(
                container=query_result.get(DBFields.container),
                status_id=query_result.get(DBFields.id),
            )

        # Set it last, so it will be only updated if all went OK
        if len(_query_results) and _query_results[0].get(DBFields.updated_at):
            self.last_update = _query_results[0].get(DBFields.updated_at)
