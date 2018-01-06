import pandas as pd

def buildScheduleList(pathToSchedule):       
    raw_df = pd.read_csv(pathToSchedule)
    df = pd.DataFrame()
    df = pd.DataFrame([(row[0].split()[1]).replace('-','').replace(',','') for row in raw_df.values],columns=["Game Date"])
    print(df.shape)
    df.drop_duplicates(inplace=True)
    print(df.shape)
    return df
 
def main():
    schedule = 'results/full_game_schedule-nba-2016-2017-regular.csv'
    df = buildScheduleList(schedule)

if __name__ == '__main__':
    main()
