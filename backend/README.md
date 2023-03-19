# Backend of battle game
The "battle" project is a web-based game application that allows players to create their characters, join battles, and compete on a global leaderboard.
"battle" project is designed to be a simple, yet engaging game that allows players to interact with the system and compete with one another. The code is structured to facilitate easy maintenance and future expansion of the game's features.

# Project structure
The structure of project is organized as follows:
1. app/ - The main directory containing the Flask application.
    - __init__.py: Initializes the Flask application and enables CORS for cross-origin requests, registers the blueprint, and starts the background thread for processing battles.
    - routes.py: Contains the routes and their respective view functions for handling requests related to game features such as creating players, joining battles, and fetching the leaderboard.
    - utilis.py: Contains the utility functions and objects for managing battles, such as the battle_processor, battle_queue, global_leaderboard, and global_storage.
      - The battle_processor function manages and processes battles from the battle_queue in the order they are added. It uses a ThreadPoolExecutor to execute battles concurrently for improved performance.
    - app/models - The models' folder contains the data models and their respective database schema definitions for the application. These data models represent the essential entities and relationships within the game, such as players, battles, and leaderboard rankings.
      - app/models/Player.py Player class represents a player in the game and manages their resources and attributes, such as name, gold, attack, max hit, health, luck, and score. The constructor initializes the player with the given name, a unique ID (using UUID), and randomly generated attributes like max hit and luck. It also sets initial values for gold, attack, health, and score.
      - app/models/Leaderboard.py The Leaderboard class is a generic implementation of a game leaderboard, which manages the ranking of players based on their scores. The class leverages the heapq module to maintain a sorted list of players efficiently.
      - app/models/GameStorage.py The GameStorage class manages the game's state and data storage related to players and battle reports. It provides methods for adding and retrieving players, managing battle reports, and keeping track of active and dead players.
      - app/models/Battle.py The Battle class represents a battle simulation between two players in a game. The class manages the battle process, calculates the damage during each turn, and generates a battle report upon completion.
        
2. app.py: The entry point for the Flask backend application, initializes the Flask app
3. tests/ - The directory contains tests for API, Battle, GameStorage, Leaderboard and player classes
