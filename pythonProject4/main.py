from bs4 import BeautifulSoup
import requests

response=requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movie_web_page=response.text
soup=BeautifulSoup(movie_web_page,"html.parser")
all_movies=soup.find_all(name="h3",class_="title")

movie_title=[movie.getText() for movie in all_movies]
movies=movie_title[::-1]
# print(movies)

with open("movies.txt","w",encoding="utf-8") as file1:
    for movie in movies:
        file1.write(f"{movie}\n")