import sqlite3

class Database:
    def __init__(self):
        self.connection = sqlite3.connect('infos.db')
        self.createTable()
        
    def createTable(self):
        try:
            cursor = self.connection.cursor()
            
            cursor.execute(
                """
                    CREATE TABLE IF NOT EXISTS player_infos(
                        level_id INTEGER,
                        survival_score INT,
                        casual_score INT,
                        acquired_skins 
                    )
                """
            )
            
        except Exception as error:
            return f'ERRO NO BANCO DE DADOS! {error}'
        else:
            self.connection.commit()
            self.connection.close()