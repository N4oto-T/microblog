from flask import Flask
from config import Config

app = Flask(__name__)

# 設定を読み込み、appに登録する
app.config.from_object(Config)


from app import routes
