import wikipedia

search_thing = input("What do you want to search (page/phrase)?: ").lower()

while search_thing != "":
    if search_thing == "page":
        search_page = input("Which page do you want to search?: ")
        page = wikipedia.page(search_page)
        print(page.title)
        print(page.url)
        print(wikipedia.summary(search_page))
    elif search_thing == "phrase":
        search_phrase = input("What phrase do you want to search?: ")
        print(wikipedia.search(search_thing))
        print(wikipedia.summary(search_thing))
    search_thing = input("What phrase do you want to know?: ")