class Player:
    def __init__(self, data_dict):
        self.name = data_dict["name"]
        self.age = data_dict["age"]
        self.position = data_dict["position"]
        self.team = data_dict["team"]

    @classmethod
    def add_player(cls,data_dict):
        new_team = []
        for player in data_dict:
            new_team.append(cls(player))
        return new_team

kevin = {
    "name": "Kevin Durant",
    "age": 34,
    "position": "small forward",
    "team": "Brooklyn Nets",
}
jason = {
    "name": "Jason Tatum",
    "age": 24,
    "position": "small forward",
    "team": "Boston Celtics",
}
kyrie = {
    "name": "Kyrie Irving",
    "age": 32,
    "position": "Point Guard",
    "team": "Brooklyn Nets",
}
sakuragi = {
    "name": "Sakuragi Hanamichi",
    "age": 27,
    "position": "Center",
    "team": "Shohoku",
}

players = [
    {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving", 
    	"age":32,
        "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard", 
    	"age":33,
        "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid", 
    	"age":32,
        "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]


new_team = []
for item in players:
    new_team.append(Player(item))

a = Player.add_player(players)
print(a[0].name)




