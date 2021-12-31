from facebook_page_scraper import Facebook_scraper
import argparse

def scrap(directory, page_name, posts_count):
    browser = "chrome"

    p=Facebook_scraper(page_name, posts_count, browser)
    data = p.scrap_to_json()


    filename = page_name
    p.scrap_to_csv(filename, directory)
    print('scrap is DONE')

parser = argparse.ArgumentParser(description='scrap facebook page by giving the name and the postes number')
parser.add_argument('directory', type=str, help='directory')
parser.add_argument('page_name', type=str,help='page name')
parser.add_argument('posts_count', type=int,help='posts number')
args = parser.parse_args()

if __name__=='__main__':
    print(scrap(args.directory, args.page_name, args.posts_count))