import wikipedia as wiki
print(wiki.search("Python (programming language)"))
print(wiki.suggest("Pyth")) # will the search engine on Wikipedia suggest us python if we will type only some alphabets of its spelling:
print(wiki.summary("Python (programming language)")) # will give you summery of an article on wiki
wiki.set_lang("fr")
print(wiki.summary("Python (programming language)"))

wiki.set_lang("en")
p = wiki.page("Python (programming language)")
# To get the Title
print(p.title)
# To get the url of the article
print(p.url)
# To get the full article
print(p.content)
# To get the images in the article
print(p.images)
# To get all the referals used by wiki
print(p.links)
