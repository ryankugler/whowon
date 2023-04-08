# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 16:42:22 2023

@author: Ryan Kugler
"""

from nba_api.live.nba.endpoints import boxscore

def getHomeTeamName(gameID):
    box = boxscore.BoxScore(gameID)
    boxDict = box.game.get_dict()
    homeTeam = boxDict["homeTeam"]
    teamName = homeTeam["teamCity"] + " " + homeTeam["teamName"]
    return teamName
def getAwayTeamName(gameID):
    box = boxscore.BoxScore(gameID)
    boxDict = box.game.get_dict()
    awayTeam = boxDict["awayTeam"]
    teamName = awayTeam["teamCity"] + " " + awayTeam["teamName"]
    return teamName




#def getBoxScores():
    #get yesterday's box scores
    # NAME | MIN | FG (FGM/FGA) | 3PTFG | FT | PTS | RB | AST | STL | BLK | TO | PF | +/-
    #box_dict = box.get_dict()