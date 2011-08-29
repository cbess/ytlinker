from flask import Flask
import settings

app = Flask('ytlinker')
app.config.from_object('ytlinker.settings')

import views