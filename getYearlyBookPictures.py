import requests
import os
from lxml import html
 
def getImageLinks(user_id):
    images = []
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    page = requests.get("https://www.goodreads.com/user/year_in_books/2024/" + user_id, headers=headers)
    tree = html.fromstring(page.content)
    image_links = tree.xpath('//div[@data-resource-type="Book"]/a/img')
    for i in range(0,len(image_links)):
        images.append(image_links[i].attrib['src'])
    return images
 
def main(user_id):
    directory = "./output"
    if not os.path.exists(directory):
        os.makedirs(directory)
    images = getImageLinks(user_id)
    for count in range(len(images)):
        img_data = requests.get(images[count]).content
        with open(f'./output/book{count}.jpg', 'wb') as handler:
            handler.write(img_data)
 
if __name__ == "__main__":
    import argparse
 
    parser = argparse.ArgumentParser()
    parser.add_argument('--userId', metavar='path', required=True,
                        help='Your Goodreads user id')
    args = parser.parse_args()
    main(user_id=args.userId)