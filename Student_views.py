from mysql import connector


class Dbconnect:

    def get_connected(self):
        try:
            self.connection = connector.connect(
                host="localhost",
                user="root",
                password="Abhi@123",
                database="gym_db",
            )
            return self.connection
        except Exception as e:
            return None
