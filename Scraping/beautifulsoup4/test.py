from bs4 import BeautifulSoup, element

#html为解析的页面获得html信息,为方便讲解，自己定义了一个html文件

html = """
<html>
<head>
<title>Jack_Cui</title>
</head>
<body>
<p class="title" name="blog"><b>My Blog</b></p>
<li><!--注释--></li>

<a href="http://blog.csdn.net/c406495762/article/details/58716886" class="sister" id="link1">Python3网络爬虫(一)：利用urllib进行简单的网页抓取</a><br/>
<a href="http://blog.csdn.net/c406495762/article/details/59095864" class="sister" id="link2">Python3网络爬虫(二)：利用urllib.urlopen发送数据</a><br/>
<a href="http://blog.csdn.net/c406495762/article/details/59488464" class="sister" id="link3">Python3网络爬虫(三)：urllib.error异常</a><br/>
</body>
</html>
"""

#创建Beautiful Soup对象
soup = BeautifulSoup(html,'lxml')

print(soup.title)
# print(soup.head)
# print(soup.a)
# print(soup.p)
# print(type(soup.title))
# print(soup.a.string)
# print(soup)
# print(soup.li)
# print(soup.li.string)
# print(type(soup.li.string))
# if type(soup.li.string) == element.Comment:
#      print(soup.li.string)
# print(soup.body.contents)
print(soup.find_all('a'))