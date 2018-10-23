#home stats dictionaries:
Alan_Anderson_stats = {'number': 0, 'shoe': 16, 'points': 22, 'rebounds': 12, 'assists': 12, 'steals': 3, 'blocks': 1, 'slam_dunks': 1}
Reggie_Evans_stats = {'number': 30, 'shoe': 14, 'points': 12, 'rebounds': 12, 'assists': 12, 'steals': 12, 'blocks': 12, 'slam_dunks': 7}
Brook_Lopez_stats = {'number': 11, 'shoe': 17, 'points': 17, 'rebounds': 19, 'assists': 10, 'steals': 3, 'blocks': 1, 'slam_dunks': 15}
Mason_Plumlee_stats = {'number': 1, 'shoe': 19, 'points': 26, 'rebounds': 12, 'assists': 6, 'steals': 3, 'blocks': 8, 'slam_dunks': 5}
Jason_Terry_stats = {'number': 31, 'shoe': 15, 'points': 19, 'rebounds': 2, 'assists': 2, 'steals': 4, 'blocks': 11, 'slam_dunks': 1}

#away stats dictionaries:
Jeff_Adrien_stats = {'number': 4, 'shoe': 18, 'points': 10, 'rebounds': 1, 'assists': 1, 'steals': 2, 'blocks': 7, 'slam_dunks': 2}
Bismak_Biyombo_stats = {'number': 0, 'shoe': 16, 'points': 12, 'rebounds': 4, 'assists': 7, 'steals': 7, 'blocks': 15, 'slam_dunks': 10}
DeSagna_Diop_stats = {'number': 2, 'shoe': 14, 'points': 24, 'rebounds': 12, 'assists': 12, 'steals': 4, 'blocks': 5, 'slam_dunks': 5}
Ben_Gordon_stats = {'number': 8, 'shoe': 15, 'points': 33, 'rebounds': 3, 'assists': 2, 'steals': 1, 'blocks': 1, 'slam_dunks': 0}
Brendan_Haywood_stats = {'number': 33, 'shoe': 15, 'points': 6, 'rebounds': 12, 'assists': 12, 'steals': 22, 'blocks': 5, 'slam_dunks': 12}

#home players dictionaries
home_players = {'Alan Anderson': Alan_Anderson_stats, 'Reggie Evans': Reggie_Evans_stats, 'Brook Lopez': Brook_Lopez_stats,'Mason Plumlee': Mason_Plumlee_stats,'Jason Terry': Jason_Terry_stats}

#away players dictionaries
away_players = {'Jeff Adrien': Jeff_Adrien_stats, 'Bismak Biyombo': Bismak_Biyombo_stats, 'DeSagna Diop': DeSagna_Diop_stats,'Ben Gordon': Ben_Gordon_stats,'Brendan Haywood': Brendan_Haywood_stats}

#whole game dictionary
game_dictionary = {'home': {'team_name': 'Brooklyn Nets', 'colors': 'Black, White', 'players': home_players},
                  'away': {'team_name': 'Charlotte Hornets', 'colors': 'Turquoise, Purple', 'players': away_players}}


def game_dict():
    return game_dictionary

def num_points_scored():
    100

def shoe_size():
    pass

def team_colors():
    pass

def team_names():
    pass

def player_numbers():
    pass

def player_stats():
    pass
