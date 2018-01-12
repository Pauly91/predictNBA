import pandas as pd
from ohmysportsfeedspy import MySportsFeeds
import sys



'''
Ideas
- Build a time series for each team with players and corresponding stats
- ex steph_curry_3pperc,steph_curry_trueshooting etc
- Build the same for all players all stats for a given team as time series in a CSV file along with win or lose
- Hence there are as many CSV as there are teams
- Use a teams time series and the correspoding opponents and train the network 
- obviously use previous game stats, or moving average of 3 previous, or all the three previous games per team as inputs to the 
N/W
- Do all the above and compare performance.
'''

def getInitialData(pathToData):       
    raw_df = pd.read_csv(pathToData)
    # ["['#Date/Time of Update: 2018-01-05 9:10:38 AM' - 0, '#Game Date'- 1, '#Game Time'- 2, '#Away Team ID'- 3, 
    # '#Away Team Abbr.'- 4, '#Away Team City'- 5, '#Away Team Name'- 6, '#Home Team ID'- 7, 
    # '#Home Team Abbr.'- 8, '#Home Team City'- 9, '#Home Team Name'- 10, '#Location- 11']"]
    df = pd.DataFrame()
    #print(raw_df.columns.tolist())
    #print([row[0].split()[10].replace(',','').replace("'",'') for row in raw_df.values])
    df = pd.DataFrame([row[0].split()[10].replace(',','').replace("'",'') for row in raw_df.values],columns=["Game Date"])
    df.drop_duplicates(inplace=True)
    df.to_csv('nba_team_names.csv')
    
    df = pd.DataFrame([(row[0].split()[1]).replace('-','').replace(',','').replace("'",'') for row in raw_df.values],columns=["Game Date"])
    df.drop_duplicates(inplace=True)
    df.to_csv('nba_schedule_regular_20162017.csv')
    return df
 
def getDailyPlayerStatsData(df):
    Data_query = MySportsFeeds('1.0',verbose=True)
    Data_query.authenticate('poly91', 'abel1234')
    for gameDate in df['Game Date'].tolist():
        print(gameDate)
        try:
            Output = Data_query.msf_get_data(league='nba',season='2016-2017-regular',feed='daily_player_stats',fordate=str(gameDate),format='csv',sort='player.team')
        except:
            print("errorinfo: ", sys.exc_info()[0])
            print('Issue with %d',gameDate)


def buildNBAData():
    '''
    Algorithm:
    - Iterate through files
    - Find how to work through one csv
    '''
    df = pd.read_csv('results/daily_player_stats-nba-2016-2017-regular-20161026.csv')
    columnNames = df.columns.tolist()[0].replace('[','').replace(']','').replace("'",'').replace(' ','').split(',')
    print(columnNames)
    
    # '#Date/TimeofUpdate:2018-01-088:54:52AM' - 0, '#GameDate' - 1, '#GameTeams' - 2, '#PlayerID' - 3, 
    # '#LastName' - 4, '#FirstName' - 5, '#Position' - 6, '#TeamID' - 7, '#TeamAbbr.' - 8, '#TeamCity' - 9, 
    # '#TeamName - 10'
    # 12:end is feature

def main():
    #schedule = 'results/full_game_schedule-nba-2016-2017-regular.csv'
    #df = buildScheduleList(schedule)
    

    #df = pd.read_csv('nba_schedule_regular_20162017')
    #print(df['Game Date'].tolist())
    #getDailyPlayerStatsData(df)
    data = 'results/full_game_schedule-nba-2016-2017-regular.csv'
    #buildNBAData()
    getInitialData(data)

if __name__ == '__main__':
    main()

