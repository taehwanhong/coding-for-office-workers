

#클래스


title1 = "dev"
author1 = "taehwan"
content1 = "dev easy"
view_count1 = 0

title2 = "coding"
author2 = "hong"
content2 = "coding easy"
view_count2 = 0

title3 = "venture"
author3 = "david"
content3 = "venture easy"
content3 = "venture easy"
view_count3 =  0



######## Article Clss ########
# class Article:
#     title = "dev"
#     author = "taehwan"
#     content = "dev easy"
#     view_count = 0
#
# article1 = Article()
# print(article1.title)
#
# article2 = Article()
# article2.title = "coding"
# print(article1.title)
# print(article2.title)


######## Article class with --init--

class Article:
    author = "taehwan"
    view_count = 0

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def read(self):
        self.view_count = self.view_count + 1

        #클래스안에서쓰는함수는 self 써야함.

article1 = Article("dev", "dev easy")
article2 = Article("coding", "coding easy")
article2 = Article("venture", "venture easy")


print(article1.view_count)
article1.read()
print(article1.view_count)
print(article1.title)
print(article2.title)




##### Article Class inheritance #####
# class BrunchArticle(Article):
#     source = "brunch"
#
#     def read(self):
#         self.view_count = self.view_count + 2
#         #  article class에있는 read 함수를 override  가능함.
#
# brunch_article = BrunchArticle("dev","dev easy2")
# print(brunch_article.title)
# print(brunch_article.source)
# print(brunch_article.view_count)
# brunch_article.read()
# print(brunch_article.view_count)