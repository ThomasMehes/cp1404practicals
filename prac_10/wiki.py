import wikipedia


def get_wiki_summary(title):
    """Gets wikipedia page then prints the title, summary and the URL."""
    try:
        page = wikipedia.page(title, auto_suggest=False)
        print('-'*50)
        print(f"Title: {page.title}")
        print(f"Summary: {page.summary}")
        print(f"URL: {page.url}")
        print('-' * 50)
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"The term '{title}' may refer to multiple pages. Try one of these:")
        print('\n'.join(e.options))
    except wikipedia.exceptions.PageError:
        print(f"No page found for '{title}'.")


if __name__ == "__main__":
    print("Welcome to the Wikipedia Summary Fetcher!")
    print("Enter a page title or search phrase. Leave blank to exit.")

    while True:
        user_input = input("Enter a page title or search phrase: ").strip()
        if not user_input:
            print("Exiting...")
            break
        get_wiki_summary(user_input)
