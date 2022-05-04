# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 23:51:50 2022

@author: jingw
"""

# IMDB Top 250 movies web scraping and turn into cvs file

import requests
import pandas as pd
from bs4 import BeautifulSoup
import re




'''
from 1 to 50
'''
movie_names = []
years = []
IMDB_ratings = []
votes = []
gross = []
movie_genre = []
movie_gross = []
url = 'https://www.imdb.com/search/title/?groups=top_250&sort=num_votes,desc'
headers = {'User-Agent' : 'Safari'}

movie_req = requests.get(url, headers=headers)
movie_req.raise_for_status()

movie_req_text = movie_req.text
#print(movie_req_text)
movie_soup = BeautifulSoup(movie_req_text, 'html.parser')

movie_lst = movie_soup.find_all('div', class_ = 'lister-item mode-advanced')
#print(type(movie_lst))
#print(len(movie_lst))
first_movie = movie_lst[0]
#print(first_movie)
first_movie_name = first_movie.h3.a.text
#print(first_movie_name)
first_movie_year = first_movie.h3.find('span', class_ = 'lister-item-year text-muted unbold').text
first_movie_year = first_movie_year.strip('(').strip(')')
#print(first_movie_year)
first_movie_IMDB_rating = first_movie.find('div', class_ = 'inline-block ratings-imdb-rating').text
#print(first_movie_IMDB_rating)
first_movie_votes = first_movie.find('span', attrs = {'name':'nv'}).text
#print(first_movie_votes)
first_movie_genre = first_movie.find('span', class_ = 'genre').text
#print(first_movie_genre)
first_movie_gross = first_movie.find_all('span', attrs = {'name':'nv'})[1].text
#print(first_movie_gross)
for movie_index in range(len(movie_lst)):
    movie_name = movie_lst[movie_index].h3.a.text
    movie_names.append(movie_name)
    year = movie_lst[movie_index].h3.find('span', class_ = 'lister-item-year text-muted unbold').text.strip('(').strip(')').strip('-')
    years.append(year)
    IMDB_rating = float(movie_lst[movie_index].find('div', class_ = 'inline-block ratings-imdb-rating').text)
    IMDB_ratings.append(IMDB_rating)
    vote = movie_lst[movie_index].find('span', attrs = {'name':'nv'}).text
    votes.append(vote)
    genre = movie_lst[movie_index].find('span', class_ = 'genre').text.strip('\n')
    movie_genre.append(genre)
    gross = movie_lst[movie_index].find_all('span', attrs = {'name':'nv'})[1]['data-value']
    movie_gross.append(gross)
    
runtimes = movie_soup.select('.runtime')
runtime_lst = [item.text for item in runtimes]
new_time = []
for content in runtime_lst:
    new_time.append(int(content.replace('min','').strip()))
#print(new_time)
    

new_df = pd.DataFrame({'movie name': movie_names, 'year': years, 'IMDBrating':IMDB_ratings, 
                       'votes': votes, 'genre': movie_genre, 'movieGross' : movie_gross, 'runtime': new_time})

new_df['movie name'][33] = 'Leon: The Professional'
new_df['movie name'][38] = 'WALL-E'
#print(new_df['movie name'][38])
#print(new_df['movie name'][33])

#print(new_df)
'''
from 51 to 100
'''

url2 = 'https://www.imdb.com/search/title/?groups=top_250&sort=num_votes,desc&start=51&ref_=adv_nxt'
headers2 = {'User-Agent' : 'Safari'}
movie_req2 = requests.get(url2, headers=headers)
movie_req2.raise_for_status()



movie_req_text2 = movie_req2.text

movie_soup2 = BeautifulSoup(movie_req_text2, 'html.parser')
movie_lst2 = movie_soup2.find_all('div', class_ = 'lister-item mode-advanced')


movie_names2 = []
years2 = []
IMDB_ratings2 = []
votes2 = []
gross2 = []
movie_genre2 = []
movie_gross2 = []
for movie_index2 in range(len(movie_lst2)):
    movie_name2 = movie_lst2[movie_index2].h3.a.text
    movie_names2.append(movie_name2)
    year2 = movie_lst2[movie_index2].h3.find('span', class_ = 'lister-item-year text-muted unbold').text.strip('(').strip(')').strip('-')
    years2.append(year2)
    IMDB_rating2 = float(movie_lst2[movie_index2].find('div', class_ = 'inline-block ratings-imdb-rating').text)
    IMDB_ratings2.append(IMDB_rating2)
    vote2 = movie_lst2[movie_index2].find('span', attrs = {'name':'nv'}).text
    votes2.append(vote2)
    genre2 = movie_lst2[movie_index2].find('span', class_ = 'genre').text.strip('\n')
    movie_genre2.append(genre2)
    gross2 = movie_lst2[movie_index2].find_all('span', attrs = {'name':'nv'})[1]['data-value']
    movie_gross2.append(gross2)


runtimes2 = movie_soup2.select('.runtime')
runtime_lst2 = [item.text for item in runtimes2]
new_time2 = []
for content2 in runtime_lst2:
    new_time2.append(int(content2.replace('min','').strip()))



new_df2 = pd.DataFrame({'movie name': movie_names2, 'year': years2, 'IMDBrating':IMDB_ratings2,
                        'votes': votes2, 'genre': movie_genre2, 'movieGross' : movie_gross2, 'runtime': new_time2})
#print(new_df2)
new_df2['movie name'][33] = 'Amelie'
#print(new_df2['movie name'][33])




'''
from 101 to 150
'''

url3 = 'https://www.imdb.com/search/title/?groups=top_250&sort=num_votes,desc&start=101&ref_=adv_nxt'
headers3 = {'User-Agent' : 'Safari'}
movie_req3 = requests.get(url3, headers=headers)
movie_req3.raise_for_status()



movie_req_text3 = movie_req3.text

movie_soup3 = BeautifulSoup(movie_req_text3, 'html.parser')
movie_lst3 = movie_soup3.find_all('div', class_ = 'lister-item mode-advanced')


movie_names3 = []
years3 = []
IMDB_ratings3 = []
votes3 = []
gross3 = []
movie_genre3 = []
movie_gross3 = []
for movie_index3 in range(len(movie_lst3)):
    movie_name3 = movie_lst3[movie_index3].h3.a.text
    movie_names3.append(movie_name3)
    year3 = movie_lst3[movie_index3].h3.find('span', class_ = 'lister-item-year text-muted unbold').text.strip('(').strip(')').strip('-')
    years3.append(year3)
    IMDB_rating3 = float(movie_lst3[movie_index3].find('div', class_ = 'inline-block ratings-imdb-rating').text)
    IMDB_ratings3.append(IMDB_rating3)
    vote3 = movie_lst3[movie_index3].find('span', attrs = {'name':'nv'}).text
    votes3.append(vote3)
    genre3 = movie_lst3[movie_index3].find('span', class_ = 'genre').text.strip('\n')
    movie_genre3.append(genre3)
    gross3 = movie_lst3[movie_index3].find_all('span', attrs = {'name':'nv'})[1]['data-value']
    movie_gross3.append(gross3)


runtimes3 = movie_soup3.select('.runtime')
runtime_lst3 = [item.text for item in runtimes3]
new_time3 = []
for content3 in runtime_lst3:
    new_time3.append(int(content3.replace('min','').strip()))


new_df3 = pd.DataFrame({'movie name': movie_names3, 'year': years3, 'IMDBrating':IMDB_ratings3,
                        'votes': votes3, 'genre': movie_genre3, 'movieGross' : movie_gross3, 'runtime': new_time3})



'''
from 151 to 200
'''

url4 = 'https://www.imdb.com/search/title/?groups=top_250&sort=num_votes,desc&start=151&ref_=adv_nxt'
headers4 = {'User-Agent' : 'Safari'}
movie_req4 = requests.get(url4, headers=headers)
movie_req4.raise_for_status()



movie_req_text4 = movie_req4.text

movie_soup4 = BeautifulSoup(movie_req_text4, 'html.parser')
movie_lst4 = movie_soup4.find_all('div', class_ = 'lister-item mode-advanced')


movie_names4 = []
years4 = []
IMDB_ratings4 = []
votes4 = []
gross4 = []
movie_genre4 = []
movie_gross4 = []
for movie_index4 in range(len(movie_lst4)):
    movie_name4 = movie_lst4[movie_index4].h3.a.text
    movie_names4.append(movie_name4)
    year4 = movie_lst4[movie_index4].h3.find('span', class_ = 'lister-item-year text-muted unbold').text.strip('(').strip(')').strip('-')
    years4.append(year4)
    IMDB_rating4 = float(movie_lst4[movie_index4].find('div', class_ = 'inline-block ratings-imdb-rating').text)
    IMDB_ratings4.append(IMDB_rating4)
    vote4 = movie_lst4[movie_index4].find('span', attrs = {'name':'nv'}).text
    votes4.append(vote4)
    genre4 = movie_lst4[movie_index4].find('span', class_ = 'genre').text.strip('\n')
    movie_genre4.append(genre4)
    gross4 = movie_lst4[movie_index4].find_all('span', attrs = {'name':'nv'})[1]['data-value']
    movie_gross4.append(gross4)


runtimes4 = movie_soup4.select('.runtime')
runtime_lst4 = [item.text for item in runtimes4]
new_time4 = []
for content4 in runtime_lst4:
    new_time4.append(int(content4.replace('min','').strip()))

new_df4 = pd.DataFrame({'movie name': movie_names4, 'year': years4, 'IMDBrating':IMDB_ratings4,
                        'votes': votes4, 'genre': movie_genre4, 'movieGross' : movie_gross4, 'runtime' : new_time4})



'''
from 201 to 250
'''
url5 = 'https://www.imdb.com/search/title/?groups=top_250&sort=num_votes,desc&start=201&ref_=adv_nxt'
headers5 = {'User-Agent' : 'Safari'}
movie_req5 = requests.get(url5, headers=headers)
movie_req5.raise_for_status()



movie_req_text5 = movie_req5.text

movie_soup5 = BeautifulSoup(movie_req_text5, 'html.parser')
movie_lst5 = movie_soup5.find_all('div', class_ = 'lister-item mode-advanced')


movie_names5 = []
years5 = []
IMDB_ratings5 = []
votes5 = []
gross5 = []
movie_genre5 = []
movie_gross5 = []
for movie_index5 in range(len(movie_lst5)):
    movie_name5 = movie_lst5[movie_index5].h3.a.text
    movie_names5.append(movie_name5)
    year5 = movie_lst5[movie_index5].h3.find('span', class_ = 'lister-item-year text-muted unbold').text.strip('(').strip(')').strip('-')
    years5.append(year5)
    IMDB_rating5 = float(movie_lst5[movie_index5].find('div', class_ = 'inline-block ratings-imdb-rating').text)
    IMDB_ratings5.append(IMDB_rating5)
    vote5 = movie_lst5[movie_index5].find('span', attrs = {'name':'nv'}).text
    votes5.append(vote5)
    genre5 = movie_lst5[movie_index5].find('span', class_ = 'genre').text.strip('\n')
    movie_genre5.append(genre5)
    gross5 = movie_lst5[movie_index5].find_all('span', attrs = {'name':'nv'})[1]['data-value']
    movie_gross5.append(gross5)

runtimes5 = movie_soup5.select('.runtime')
runtime_lst5 = [item.text for item in runtimes5]
new_time5 = []
for content5 in runtime_lst5:
    new_time5.append(int(content5.replace('min','').strip()))


new_df5 = pd.DataFrame({'movie name': movie_names5, 'year': years5, 'IMDBrating':IMDB_ratings5,
                        'votes': votes5, 'genre': movie_genre5, 'movieGross' : movie_gross5, 'runtime':new_time5})




final_df = pd.concat([new_df,new_df2,new_df3,new_df4,new_df5])
new_years = []
for year in final_df['year']:
    if year == int:
        new_years.append(year)
    else:
        year_needed = int(re.search(r'\d+', year).group())
        new_years.append(year_needed)
#print(new_years)
final_df['year'] = new_years
#print(final_df)

new_vote = []
for vote in final_df['votes']:
    new_vote.append(int(vote.replace(',','')))

final_df['votes'] = new_vote

new_gross = []
for number in final_df['movieGross']:
    new_gross.append(int(number.replace(',','')))

final_df['movieGross'] = new_gross

final_df = final_df[final_df['movieGross'] > 250]


final_genre = []
for i in final_df['genre']:
    genre_needed = i.split(',')[0].strip()
    final_genre.append(genre_needed)
final_df['genre'] = final_genre
#print(final_genre)
final_df.to_csv('final_IMDB_dataset.csv', index=False)





