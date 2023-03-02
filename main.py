import feedparser, time

URL = "https://v2.velog.io/rss/minkyu__k"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 10

markdown_text = """
## 📚 Latest Blog Post
<base target="_blank">
<ul>
"""  # list of blog posts will be appended here

for idx, feed in enumerate(RSS_FEED['entries']):
    if idx > MAX_POST:
        break
    else:
        feed_date = feed['published_parsed']
        link = feed['link']
        title = feed['title']
        markdown_text += f"<li><a href=\"{link}\">{time.strftime('%Y/%m/%d', feed_date)} - {title}</a></li>"
        
markdown_text +="</ul>"
readme = ""
f = open("README.md", mode="w", encoding="utf-8")
lines = f.readlines()
for line in lines:
    readme += line
    
f.write(readme)
f.write(markdown_text)
f.close()
