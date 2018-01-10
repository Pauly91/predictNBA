from ohmysportsfeedspy import MySportsFeeds

Data_query = MySportsFeeds('1.0',verbose=True)
Data_query.authenticate('poly91', 'abel1234')
Output = Data_query.msf_get_data(league='nba',season='2016-2017-regular',feed='daily_player_stats',fordate='20161202',format='json',sort='player.team')
#Output = Data_query.msf_get_data(league='nba',season='2016-2017-regular',feed='full_game_schedule',format='csv')
#Output = Data_query.msf_get_data(league='nba',season='2016-2017-regular',feed='game_boxscore',format='csv')
# 20161025
print(Output)


'''

Get the dates from the full_game_schedule and iterate through the dates with the daily_player_stats with sort = player.team

Sort the data based on teams, and make different CSV files.

'''
