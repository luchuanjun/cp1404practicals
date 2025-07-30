import wikipedia

while True:
    title = input("Enter page title: ")
    if not title:
        print("Thank you.")
        break
    try:
        page = wikipedia.page(title, auto_suggest=False)
        print(page.title)
        print(wikipedia.summary(title, sentences=2))
        print(page.url)
    except wikipedia.exceptions.DisambiguationError as e:
        print("We need a more specific title. Try one of the following:")
        print(e.options)
    except wikipedia.exceptions.PageError:
        print("Page not found. Try another.")