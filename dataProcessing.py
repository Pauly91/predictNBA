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

def buildScheduleList(pathToSchedule):       
    raw_df = pd.read_csv(pathToSchedule)
    df = pd.DataFrame()
    df = pd.DataFrame([(row[0].split()[1]).replace('-','').replace(',','').replace("'",'') for row in raw_df.values],columns=["Game Date"])
    df.drop_duplicates(inplace=True)
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

def main():
    #schedule = 'results/full_game_schedule-nba-2016-2017-regular.csv'
    #df = buildScheduleList(schedule)
    #df.to_csv('nba_schedule_regular_20162017')
    df = pd.read_csv('nba_schedule_regular_20162017')
    print(df['Game Date'].tolist())
    getDailyPlayerStatsData(df)
if __name__ == '__main__':
    main()

