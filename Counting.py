def top3FileName(urls):
    dict = {}
    # get the file name
    for url in urls:
        filename = url[url.rfind("/") + 1:]
        if filename in dict.keys():
            dict[filename] += 1
        else:
            dict[filename] = 1
    # sort the dict
    L = sorted(dict.items(), key=lambda item: item[1], reverse=True)
    L = L[:3]
    return L


# testing data
urls = [
    "http://www.google.com/a.txt",
    "http://www.google.com.tw/a.txt",
    "http://www.google.com/download/c.jpg",
    "http://www.google.co.jp/a.txt",
    "http://www.google.com/b.txt",
    "https://facebook.com/movie/b.txt",
    "http://yahoo.com/123/000/c.jpg",
    "http://gliacloud.com/haha.png",
    ]
print(top3FileName(urls))