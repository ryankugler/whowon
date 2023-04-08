# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 15:20:55 2023

@author: Ryan Kugler
"""

import boxScoreHelper
import requests

######
#Todo: Get all of yesterday's games
#Put them into a list/dict or find way to get gameID
#####

from nba_api.live.nba.endpoints import boxscore
from nba_api.live.nba.endpoints import scoreboard
from datetime import date, timedelta
#box = boxscore.BoxScore('0022000196') 

score = scoreboard.ScoreBoard()
games = scoreboard.ScoreBoard().get_dict()
gameList = games["scoreboard"]["games"]

##############################
##### Previous Game Data #####
##############################

today = date.today()
yesterday = today - timedelta(1)

print (score.score_board_date)

score.score_board_date = yesterday

print(score.score_board_date)
