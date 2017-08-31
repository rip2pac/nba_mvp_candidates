from data_scraping import *
import pprint

stat_list = []
for year in range(0,62):
    #6 to 19
    stat_list_temp = []
    for stat in range(6,20):

        try:
            
            mvp_winner_stat = float(players_data[year][0][stat])
            second_place_stat = float(players_data[year][1][stat])
            third_place_stat = float(players_data[year][2][stat])
        
            if mvp_winner_stat > second_place_stat and mvp_winner_stat > third_place_stat:
                stat_list_temp.append(stat)
        except:
            pass
            
    stat_list.append(stat_list_temp)
    
for x in stat_list:
    if stat_list.count(x) >= 2:
        print(x)
