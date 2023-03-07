import feedparser, time

URL = "https://v2.velog.io/rss/minkyu__k"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 10

markdown_text = """
## 📚 Latest Posts
> 👉 `cmd ⌘`(Windows `ctrl`) + `click`
<ul>
"""  # list of blog posts will be appended here

for idx, feed in enumerate(RSS_FEED['entries']):
    if idx > MAX_POST:
        break
    feed_date = feed['published_parsed']
    link = feed['link']
    title = feed['title']
    markdown_text += f"<li>{time.strftime('%Y. %m. %d.', feed_date)} <a target='_blank' href=\"{link}\">{title}</a></li>"
        
markdown_text += """
</ul>
<img src=\"https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fgoldcrestwilma%2Fhit-counter&count_bg=%2379C83D&title_bg=%23555555&icon=github.svg&icon_color=%23E7E7E7&title=hits&edge_flat=false\"/>
"""

f = open("README.md", mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
