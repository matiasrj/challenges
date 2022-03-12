import os

from pydantic import BaseSettings
from dotenv import load_dotenv
load_dotenv()


class Settings(BaseSettings):

    _db_name: str = os.getenv('DB_NAME')
    db_user: str = os.getenv('DB_USER')
    db_pass: str = os.getenv('DB_PASS')
    db_host: str = os.getenv('DB_HOST')
    db_port: str = os.getenv('DB_PORT')

    # getter for testing
    @property 
    def db_name(self):
        if os.getenv('RUN_ENV') == 'test':
            return 'test_' + self._db_name + 'b'

        return self._db_name