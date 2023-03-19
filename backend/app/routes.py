import json
from flask import Blueprint, request, jsonify, Response
from app.models import Player
from app.utilis import global_leaderboard, battle_queue, global_storage

game_routes = Blueprint('game_routes', __name__)


class PlayerEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, '__dict__'):
            return obj.__dict__
        return super(PlayerEncoder, self).default(obj)


@game_routes.route('/create-player', methods=['POST'])
def create_player():
    data = request.json
    if 'name' not in data:
        return jsonify({"error": "Missing player name"}), 400

    player = Player.create(data['name'])
    global_storage.add_player(player)

    return jsonify({"player_id": player.id, "player_name": player.name}), 201


@game_routes.route('/get-players', methods=['GET'])
def get_active_players():
    players = global_storage.active_players
    response_data = json.dumps(players, cls=PlayerEncoder)
    return Response(response_data, mimetype='application/json'), 200


@game_routes.route('/get-dead-players', methods=['GET'])
def get_dead_players():
    players = global_storage.dead_players
    response_data = json.dumps(players, cls=PlayerEncoder)
    return Response(response_data, mimetype='application/json'), 200


@game_routes.route('/get-reports', methods=['GET'])
def get_reports():
    reports = global_storage.get_reports()
    return jsonify(reports), 200


@game_routes.route('/get-last-report', methods=['GET'])
def get_last_report():
    return jsonify(global_storage.get_last_report()), 200


@game_routes.route('/submit-battle', methods=['POST'])
def submit_battle():
    data = request.json
    if 'attacker_id' not in data or 'defender_id' not in data:
        return jsonify({"error": "Missing attacker_id or defender_id"}), 400

    attacker = global_storage.get_player_by_id(data['attacker_id'])
    defender = global_storage.get_player_by_id(data['defender_id'])

    if attacker is None or defender is None:
        return jsonify({"error": "Wrong attacker or defender id"}), 400

    battle_queue.put({"attacker": attacker, "defender": defender})
    return jsonify({"message": "Battle request submitted"}), 202


@game_routes.route('/leaderboard', methods=['GET'])
def retrieve_leaderboard():
    num_entries = request.args.get('num_entries', default=None, type=int)
    leaderboard_data = global_leaderboard.get_leaderboard(num_entries)
    return jsonify(leaderboard_data), 200
