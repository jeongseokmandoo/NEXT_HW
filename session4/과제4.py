
import requests as req
from bs4 import BeautifulSoup
import pandas as pd

url_target = "https://opentutorials.org/course/1"

res = req.get(url_target)

soup = BeautifulSoup(res.text, 'html.parser')

li_name = soup.select('div.name.time > strong')
li_time = soup.select('div.name.time > a > time')
li_comments = soup.select('div.comment_content')

li_name_final = [e.text.strip() for e in li_name]
li_time_final = [e.text.strip() for e in li_time]
li_comments_final = [e.text.strip() for e in li_comments]

context = {"nmae" : li_name_final, "time" : li_time_final, "comments" : li_comments_final}

result_table = pd.DataFrame(context)
print(result_table)