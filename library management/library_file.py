import requests
def get_book(query,limit = 10):
    url = f"https://openlibrary.org/search.json?q={query}&limit={limit}"
    response = requests.get(url)
    #print(response.status_code)
    if response.status_code == 200:
        data = response.json()
        if len(data["docs"]) == 0:
            return "No book found"

        book = data["docs"][0]

        title = book.get('title')
        author = ", ".join(book.get('author_name', []))
        year = book.get('first_publish_year')
        edition_count = book.get('edition_count')
        ebook_access = book.get('ebook_access','N/A')
        work_key = book.get("key", None)
        other_values = []
        link = (
            book.get("lending_edition") or
            book.get("lending_edition_s") or
            (book.get("edition_key")[0] if "edition_key" in book and book["edition_key"] else None) or
            book.get("cover_edition_key")
        )
        # print("DEBUG RESULT FROM get_book():",title,author,year,edition_count,ebook_access)

        return title, author, year, edition_count, ebook_access, link, work_key, *other_values
        # return {
        #     "title": None,
        #     "author": author,
        #     "year": year,
        #     "edition_count": edition_count,
        #     "ebook_access": ebook_access,
        #     "link": link,
        #     "work_key": work_key
        # }

    else :
        print('CHECK YOUR INTERNET CONNECTION')
