# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import csv
import crawler


def crawl(start_url: str):
    # Use a breakpoint in the code line below to debug your script.
    print(f'start crawling {start_url}')  # Press Strg+F8 to toggle the breakpoint.

    crawler_fetcher = crawler.ArticleFetcher(start_url)
    pages = crawler_fetcher.fetch__all__pages()  # --> fetch_all _pages return list of list of articles ()

    counter = 0

    # flatten with generator-support):
    articles = (article for pg in pages for article in pg)

    for a in articles:

        counter += 1
        if counter == 8:
            break
        print(a.emoji + ": " + a.title)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    url = 'https://python.beispiel.programmierenlernen.io/'
    csv_file_name = 'crawler_output_generator.csv'
    crawl(url)

    print(f'Save to file {csv_file_name} ...')
    fetcher = crawler.ArticleFetcher(url)
    fetcher.write_to_file(csv_file_name, 15)

    print(f'Read from file {csv_file_name} ...')
    result = fetcher.read_from_file(csv_file_name)

    print(f'{len(result)} entries retrieved:')
    for art in result:
        print(f'{art.emoji} {art.title}\n{art.content}\n{art.title}')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
