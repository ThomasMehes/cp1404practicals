import wikipedia

prompt = 'What page would you like to search for?'

print(prompt)
title = input('>>> ')
while title != '':
    try:
        page = wikipedia.page(title, auto_suggest=False)
        print("-" * 50)
        print(page.title)
        print(f"Summary: {page.summary}")
        print(f"Webpage link: {page.url}")
        print("-" * 50)
    except wikipedia.exceptions.DisambiguationError as e:
        print('Search term is too ambiguous, please choose an option from the following list instead: ')
        print(e.options)
    except wikipedia.exceptions.PageError:
        print('Page not found')

    print(prompt)
    title = input('>>> ')
