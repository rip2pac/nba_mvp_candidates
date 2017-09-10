from bs4 import BeautifulSoup
import requests
import pprint

players_data = []

for year_count in range(0,62) :

        try:
                #print(1956+year_count)

                r = requests.get("https://www.basketball-reference.com/awards/awards_"+ str(1956+year_count) + ".html")
                data = r.text
                #use requests to make python read html code from the website
                #convert the html code to text 

                soup = BeautifulSoup(data, "html.parser")
                #create a bs object and store the html code inisde it
                #this object will be used to interpreting/segmenting the html code
                #navigate around the bs object using html.parser 

                mvp_table = soup.find('table', id='mvp')
                #parse through the html code inside the soup object (hereon simply called "html code")
                #locate a specific table with id='mvp' which is our table of interest.
                #this is the table we will use to gather mvp data from 

                mvp_table_str = str(mvp_table)
                #stringify the html code for the table of interest 

                soup2 = BeautifulSoup(mvp_table_str, "html.parser")
                #we will create another bs object to play with the newly found mvp table

                heading_1_list = []
                #create a list to contain the headings in
                for th in soup2.findAll('tr', limit=2)[1].findAll('th'):
                        th_line = th.getText()
                        heading_1_list.append(th_line)
                #looking at the html code for the mvp table, we understand that the second row of the
                #table contains the headings that we are looking for
                #we will parse through the table's html and find all the rows of the table (aka tagged as 'tr')
                #we will look for the second row by going to the returned list from above and locate the second 
                #item on the list ([0,1,2,3...])
                #on that particular line, locate headings of that row (aka tagged as 'th')
                #get the text value of the content inside the 'th' tags
                #append it to a list along with other headings of the row

                heading_2_list = []
                for row in range(0,3):
                        #print(row)
                        temp_value_list=[]
                        for th in soup2.findAll('tr', limit=3+row)[2+row]:
                                row_value = th.getText()
                                temp_value_list.append(row_value)
                        heading_2_list.append(temp_value_list)
                        
                #pprint.pprint(heading_2_list)
                players_data.insert(year_count, heading_2_list)

        except:
                pass
