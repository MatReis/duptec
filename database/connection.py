import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Connection:
    def __init__(self, db_url=None):
        if not db_url:
            exec(open('.env').read())
            print("ambiente -> ", os.getenv("SQL_STRING_CONECTION"))
            db_url = os.getenv('SQL_STRING_CONECTION')

        print('URL: ', db_url)    
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)
    
    def get_session(self):
        try:
            return self.Session()
        except Exception as e:
            print(f"Erro ao obter a sessão: {e}")
