from collections import Counter

urls = [ "http://www.google.com/a.txt",
        "http://www.google.com.tw/a.txt",
        "http://www.google.com/download/c.jpg",
        "http://www.google.co.jp/a.txt",
        "http://www.google.com/b.txt",
        "https://facebook.com/movie/b.txt",
        "http://yahoo.com/123/000/c.jpg",
        "http://gliacloud.com/haha.png", ]

urls_filename = []
for url in urls:
    urls_filename.append(url.split('/')[-1])
word_count = Counter(urls_filename)
top_three = word_count.most_common(3)
for url in top_three:
    print(url[0],url[1])