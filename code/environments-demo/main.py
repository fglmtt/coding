import requests


def search_jokes(term):
    """
    Search for jokes that contain a term. Return a list of strings

    >>> isinstance(search_jokes("cat"), list)
    True
    """
    response = requests.get(
        "https://icanhazdadjoke.com/search",
        params={"term": term},
        headers={"Accept": "application/json"},
    )
    response.raise_for_status()
    return [result["joke"] for result in response.json()["results"]]


def main():
    term = input("Keyword: ")
    jokes = search_jokes(term)
    if not jokes:
        print("No jokes found")
    for number, joke in enumerate(jokes, 1):
        print(f"{number}. {joke}")


if __name__ == "__main__":
    main()
