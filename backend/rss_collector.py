import feedparser

rss_urls = [
    "https://feeds.feedburner.com/TechCrunch",
    "https://www.theverge.com/rss/index.xml"
]

for rss in rss_urls:

    feed = feedparser.parse(rss)

    print("\n" + "=" * 50)
    print(feed.feed.title)
    print("=" * 50)

    for entry in feed.entries[:5]:
        print(entry.title)
        print(entry.link)
        print()
