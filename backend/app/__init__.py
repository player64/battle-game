from flask import Flask
from threading import Thread
from app.routes import game_routes
from app.utilis import battle_processor, battle_queue, global_leaderboard, global_storage
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app, resources={r'*': {'origins': '*'}})
    app.register_blueprint(game_routes)
    battle_processor_thread = Thread(target=battle_processor, daemon=True)
    battle_processor_thread.start()

    return app
