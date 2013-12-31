from jinja2 import Environment, FileSystemLoader
import json

env = Environment(loader=FileSystemLoader('templates'))

def make_index():
   template = env.get_template('index.html')
   with open('text/home_text.html','r') as f:
      home_text = f.read()
   output = template.render(selected="home",home_text=home_text)
   with open('site/index.html','w') as f:
      f.write(output)

def make_roster():
   template = env.get_template('roster.html')
   with open('data/roster.json','r') as f:
      team = json.load(f)
   output = template.render(selected="roster",team=team)
   with open('site/roster.html','w') as f:
      f.write(output)

def make_news():
   template = env.get_template('news.html')
   output = template.render(selected="news")
   with open('site/news.html','w') as f:
      f.write(output)

def make_alumni():
   template = env.get_template('alumni.html')
   output = template.render(selected="alumni")
   with open('site/alumni.html','w') as f:
      f.write(output)

def make_photos():
   template = env.get_template('photos.html')
   output = template.render(selected="photos")
   with open('site/photos.html','w') as f:
      f.write(output)

def make_schedule():
   template = env.get_template('schedule.html')
   with open('data/schedule.json','r') as f:
      schedule = json.load(f)
   output = template.render(selected="schedule", schedule=schedule)
   with open('site/schedule.html','w') as f:
     f.write(output)

def main():
   make_index()
   make_roster()
   make_news()
   make_alumni()
   make_photos()
   make_schedule()

if __name__ == '__main__':
   main()
