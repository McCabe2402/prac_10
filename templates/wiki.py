import wikipedia


def get_summary(title):
    """Get and print the title, summary and URL of a wiki page"""
    try:
        page = wikipedia.page(title, auto_suggest=False)
        print("Title:", page.title)
        print("Summary:", page.summary)
        print("URL:", page.url)
    except wikipedia.DisambiguationError as e:
        print(f"DisambiguationError: {e.options}")


def main():
    user_input = input("Enter a page title or search phrase (blank to exit): ").strip()

    while user_input:
        # Get and print the summary for the entered title or search phrase
        get_summary(user_input)
        print("\n")

        # Prompt the user for input again
        user_input = input("Enter a page title or search phrase (blank to exit): ").strip()


if __name__ == "__main__":
    main()
