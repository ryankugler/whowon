# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 15:20:55 2023

@author: Ryan Kugler
"""

import boxScoreHelper

######
#Todo: Get all of yesterday's games
#Put them into a list/dict or find way to get gameID
#####

from nba_api.live.nba.endpoints import boxscore
from nba_api.live.nba.endpoints import scoreboard
#box = boxscore.BoxScore('0022000196') 

score = scoreboard.ScoreBoard()
games = scoreboard.ScoreBoard().get_dict()

gameList = games["scoreboard"]["games"]


#boxDict = box.game.get_dict()


