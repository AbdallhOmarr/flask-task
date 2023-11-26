from flask import Flask, render_template
from config import config
from flask_mysqldb import MySQL
import os 
from .models import init_models_first_time
app = Flask(__name__)
mysql = MySQL()

config_name='default'
app.config.from_object(config[config_name])

from .main import main as main_blueprint
app.register_blueprint(main_blueprint)


mysql.init_app(app)


@app.cli.command('init_db')
def init_db_cmd():
    init_models_first_time()
    
# Add the command to the Flask CLI
# app.cli.add_command(cli.Command("init_db", callback=init_db_command))



