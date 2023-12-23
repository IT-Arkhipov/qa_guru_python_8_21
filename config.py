import os
from pydantic import BaseModel
from dotenv import load_dotenv


class Settings(BaseModel):
    user_name: str
    access_key: str
    bs_app: str


load_dotenv()
settings = Settings(
    user_name='anrihevel_6Z04ct',
    access_key='kYjno9yicFJHqtcVvCyH',
    bs_app="bs://c6e4dfaf8a84d45e690c236928c13af186fd32ad"
)
