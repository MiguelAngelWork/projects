kevin = {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
}
jason = {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
}
kyrie = {
    	"name": "Kyrie Irving", 
    	"age":32,
        "position": "Point Guard", 
    	"team": "Brooklyn Nets"
}
class Player:
    
    player_list=[]
    def __init__(self, playerDict):
        self.name=playerDict['name']
        self.age = playerDict['age']
        self.position =playerDict['position']
        self.team = playerDict['team']
        self.player_list.append(playerDict['name']) # add player names to array
        
        
    @classmethod
    def get_team(cls,team_list):
        for each_name in team_list:
            Player(each_name)
            print(each_name['name'])
      


# kevinPlayer = Player(kevin)
# print(kevinPlayer.age)
# jasonPlayer = Player(jason)

# new_team = []
# for each_player in Player.player_list:
#     new_team.append(each_player.name)

player_list= [
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
    }]   
    
    
# print(player_list)
Player.get_team(player_list)
print(Player.player_list)



