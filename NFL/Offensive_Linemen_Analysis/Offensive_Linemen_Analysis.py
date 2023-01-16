import pandas as pd
import numpy as np
import os


def get_week_data():
    weeks = []
    for filenames in os.walk('./input'):
        for filename in filenames[2]:
            if filename.find('week') != -1:
                weeks.append(filename)
    return weeks


if __name__ == "__main__":

    game_df = pd.read_csv('./input/games.csv')
    pffScoutingData_df = pd.read_csv('./input/pffScoutingData.csv')
    players_df = pd.read_csv('./input/players.csv')
    plays_df = pd.read_csv('./input/plays.csv')
    week_names = get_week_data()
    week_df = pd.DataFrame
    for week in week_names:
        df = pd.read_csv('./input/' + week)
        week_df = pd.concat([df])
    game_scores_df = pd.read_csv('./input/spreadspoke_scores.csv')

    game_scores_df = game_scores_df.loc[(game_scores_df['schedule_season']==2021) &
                                        (game_scores_df['schedule_week'].isin(['1','2','3',
                                                                               '4','5','6',
                                                                               '7', '8']))]

    game_scores_df = game_scores_df[['schedule_week','team_home','team_away',
                                     'score_home', 'score_away']]

    game_scores_df['team_home']= np.where(game_scores_df['team_home']=='Miami Dolphins', 'MIA',
                                 np.where(game_scores_df['team_home']=='Oakland Raiders', 'OAK',
                                 np.where(game_scores_df['team_home']=='Denver Broncos','DEN',
                                 np.where(game_scores_df['team_home']=='Buffalo Bills', 'BUF',
                                 np.where(game_scores_df['team_home']=='New York Jets', 'NYJ',
                                 np.where(game_scores_df['team_home']=='New York Giants', 'NYG',
                                 np.where(game_scores_df['team_home']=='Dallas Cowboys', 'DAL',
                                 np.where(game_scores_df['team_home']=='Philadelphia Eagles', 'PHI',
                                 np.where(game_scores_df['team_home']=='Pittsburgh Steelers', 'PIT',
                                 np.where(game_scores_df['team_home']=='Minnesota Vikings', 'MIN',
                                 np.where(game_scores_df['team_home']=='Cincinnati Bengals', 'CIN',
                                 np.where(game_scores_df['team_home']=='Carolina Panthers', 'CAR',
                                 np.where(game_scores_df['team_home']=='Tampa Bay Buccaneers', 'TB',
                                 np.where(game_scores_df['team_home']=='Atlanta Falcons', 'ATL',
                                 np.where(game_scores_df['team_home']=='New Orleans Saints', 'NO',
                                 np.where(game_scores_df['team_home']=='Seattle Seahawks','SEA',
                                 np.where(game_scores_df['team_home']=='Kansas City Chiefs', 'KC',
                                 np.where(game_scores_df['team_home']=='Washington Football Team', 'WAS',
                                 np.where(game_scores_df['team_home']=='Tennessee Titans', 'TEN',
                                 np.where(game_scores_df['team_home']=='Indianapolis Colts', 'IND',
                                 np.where(game_scores_df['team_home']=='Houston Texans','HOU',
                                 np.where(game_scores_df['team_home']=='Green Bay Packers', 'GB',
                                 np.where(game_scores_df['team_home']=='Detroit Lions', 'DET',
                                 np.where(game_scores_df['team_home']=='New England Patriots', 'NE',
                                 np.where(game_scores_df['team_home']=='Los Angeles Rams', 'LA',
                                 np.where(game_scores_df['team_home']=='Los Angeles Chargers', 'LAC',
                                 np.where(game_scores_df['team_home']=='Las Vegas Raiders', 'LV',
                                 np.where(game_scores_df['team_home']=='Jacksonville Jaguars', 'JAX',
                                 np.where(game_scores_df['team_home']=='Cleveland Browns', 'CLE',
                                 np.where(game_scores_df['team_home']=='Baltimore Ravens', 'BAL',
                                 np.where(game_scores_df['team_home']=='Chicago Bears', 'CHI',
                                 np.where(game_scores_df['team_home']=='Arizona Cardinals', 'ARI', 
                                 np.where(game_scores_df['team_home']=='San Francisco 49ers', 'SF',game_scores_df['team_home'])))))))))))))))))))))))))))))))))

    game_scores_df['team_away']= np.where(game_scores_df['team_away']=='Miami Dolphins', 'MIA',
                                 np.where(game_scores_df['team_away']=='Oakland Raiders', 'OAK',
                                 np.where(game_scores_df['team_away']=='Denver Broncos','DEN',
                                 np.where(game_scores_df['team_away']=='Buffalo Bills', 'BUF',
                                 np.where(game_scores_df['team_away']=='New York Jets', 'NYJ',
                                 np.where(game_scores_df['team_away']=='New York Giants', 'NYG',
                                 np.where(game_scores_df['team_away']=='Dallas Cowboys', 'DAL',
                                 np.where(game_scores_df['team_away']=='Philadelphia Eagles', 'PHI',
                                 np.where(game_scores_df['team_away']=='Pittsburgh Steelers', 'PIT',
                                 np.where(game_scores_df['team_away']=='Minnesota Vikings', 'MIN',
                                 np.where(game_scores_df['team_away']=='Cincinnati Bengals', 'CIN',
                                 np.where(game_scores_df['team_away']=='Carolina Panthers', 'CAR',
                                 np.where(game_scores_df['team_away']=='Tampa Bay Buccaneers', 'TB',
                                 np.where(game_scores_df['team_away']=='Atlanta Falcons', 'ATL',
                                 np.where(game_scores_df['team_away']=='New Orleans Saints', 'NO',
                                 np.where(game_scores_df['team_away']=='Seattle Seahawks','SEA',
                                 np.where(game_scores_df['team_away']=='Kansas City Chiefs', 'KC',
                                 np.where(game_scores_df['team_away']=='Washington Football Team', 'WAS',
                                 np.where(game_scores_df['team_away']=='Tennessee Titans', 'TEN',
                                 np.where(game_scores_df['team_away']=='Indianapolis Colts', 'IND',
                                 np.where(game_scores_df['team_away']=='Houston Texans','HOU',
                                 np.where(game_scores_df['team_away']=='Green Bay Packers', 'GB',
                                 np.where(game_scores_df['team_away']=='Detroit Lions', 'DET',
                                 np.where(game_scores_df['team_away']=='New England Patriots', 'NE',
                                 np.where(game_scores_df['team_away']=='Los Angeles Rams', 'LA',
                                 np.where(game_scores_df['team_away']=='Los Angeles Chargers', 'LAC',
                                 np.where(game_scores_df['team_away']=='Las Vegas Raiders', 'LV',
                                 np.where(game_scores_df['team_away']=='Jacksonville Jaguars', 'JAX',
                                 np.where(game_scores_df['team_away']=='Cleveland Browns', 'CLE',
                                 np.where(game_scores_df['team_away']=='Baltimore Ravens', 'BAL',
                                 np.where(game_scores_df['team_away']=='Chicago Bears', 'CHI',
                                 np.where(game_scores_df['team_away']=='Arizona Cardinals', 'ARI', 
                                 np.where(game_scores_df['team_away']=='San Francisco 49ers', 'SF',game_scores_df['team_away'])))))))))))))))))))))))))))))))))

    print('hey')
