from jinja2 import Environment, FileSystemLoader
import json
import markdown

env = Environment(loader=FileSystemLoader('templates'))

tabs = [('Home','index'),
        ('News','news'),
        ('Roster','roster'),
        ('Alumni','alumni'),
        ('Contact','contact'),
        ('Schedule','schedule')
        ]

def make_index():
   template = env.get_template('index.html')
   with open('text/home_text.text','r') as f:
      home_text = markdown.markdown(f.read(),['extra'])
   output = template.render(tabs=tabs,selected="index",home_text=home_text)
   with open('site/index.html','w') as f:
      f.write(output)

def make_roster():
   template = env.get_template('roster.html')
   with open('data/roster.json','r') as f:
      team = json.load(f)
   output = template.render(tabs=tabs,selected="roster",team=team)
   with open('site/roster.html','w') as f:
      f.write(output)

def make_news():
   template = env.get_template('news.html')
   with open('text/news_text.text','r') as f:
     news_text = markdown.markdown(f.read(),['extra'])
   with open('data/newsletters.json') as f:
     newsletters = json.load(f)
   output = template.render(tabs=tabs,selected="news",news_text=news_text,newsletters=newsletters)
   with open('site/news.html','w') as f:
      f.write(output)

def make_alumni():
   template = env.get_template('alumni.html')
   with open('text/alumni_text.text','r') as f:
     alumni_text = markdown.markdown(f.read(),['extra'])
   with open('data/fops.json','r') as f:
     fops_officers = json.load(f)
   output = template.render(tabs=tabs,selected="alumni",
       alumni_text=alumni_text,fops_officers=fops_officers)
   with open('site/alumni.html','w') as f:
      f.write(output)

def make_contact():
   template = env.get_template('contact.html')
   with open('text/contact_text.text','r') as f:
     contact_text = markdown.markdown(f.read(),['extra'])
   output = template.render(tabs=tabs,selected="contact",
       contact_text = contact_text)
   with open('site/contact.html','w') as f:
      f.write(output)

def make_schedule():
   template = env.get_template('schedule.html')
   with open('data/schedule.json','r') as f:
      seasons = json.load(f)
   output = template.render(tabs=tabs,selected="schedule", seasons=seasons)
   with open('site/schedule.html','w') as f:
     f.write(output)

def main():
   make_index()
   make_roster()
   make_news()
   make_alumni()
   make_contact()
   make_schedule()

if __name__ == '__main__':
   main()
