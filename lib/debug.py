# game.py
class Game:
    def __init__(self, title):
        if not isinstance(title, str) or len(title) == 0:
            raise ValueError("Title must be a non-empty string.")
        self._title = title
        self._results = []

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        raise AttributeError("Title attribute is immutable and cannot be changed.")

    def results(self):
        return self._results

    def players(self):
        return list(set(result.player for result in self._results))

    def average_score(self, player):
        scores = [result.score for result in self._results if result.player == player]
        if not scores:
            return None
        return sum(scores) / len(scores)


# player.py
class Player:
    def __init__(self, username):
        if not isinstance(username, str) or not (2 <= len(username) <= 16):
            raise ValueError("Username must be a string between 2 and 16 characters.")
        self._username = username
        self._results = []

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise ValueError("Username must be a string between 2 and 16 characters.")
        self._username = value

    def results(self):
        return self._results

    def games_played(self):
        return list(set(result.game for result in self._results))

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        return sum(1 for result in self._results if result.game == game)

    @classmethod
    def highest_scored(cls, game):
        players = [result.player for result in game.results()]
        if not players:
            return None
        return max(players, key=lambda player: game.average_score(player))


# result.py
class Result:
    def __init__(self, player, game, score):
        if not isinstance(player, Player):
            raise ValueError("Player must be an instance of Player class.")
        if not isinstance(game, Game):
            raise ValueError("Game must be an instance of Game class.")
        if not isinstance(score, int) or not (1 <= score <= 5000):
            raise ValueError("Score must be an integer between 1 and 5000.")
        self._player = player
        self._game = game
        self._score = score
        player._results.append(self)
        game._results.append(self)

    @property
    def player(self):
        return self._player

    @property
    def game(self):
        return self._game

    @property
    def score(self):
        return self._score
