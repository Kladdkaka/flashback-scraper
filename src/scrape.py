from typing import List

import typer
import requests
from bs4 import BeautifulSoup, Tag
from fake_useragent import UserAgent

app = typer.Typer()


@app.command()
def thread(thread_id: int, user_agent: str = None):
    typer.echo(f"scrape thread: {thread_id}")

    page_id = 1

    if user_agent is None:
        user_agent = UserAgent().chrome

    headers = {'User-Agent': user_agent}

    r = requests.get(f'https://www.flashback.org/t{thread_id}p{page_id}', headers=headers)
    html = r.content
    soup = BeautifulSoup(html, features='lxml')
    print(soup)
    last_page_id = int(soup.find('span', class_='input-page-jump').attrs['data-total-pages'])

    print(last_page_id)

    print()

    # Actually a ResultSet but who cares
    post_elements: List[Tag] = soup.find('div', id='posts').find_all('div', class_='post')

    for e in post_elements:
        post_id = e.attrs['data-postid']

        post_user_username = e.find('a', class_='post-user-username').text.strip()
        post_user_title = e.find('div', class_='post-user-title').text.strip()
        post_user_avatar = None

        avatar_e = e.find('div', class_='post-user-avatar')
        if avatar_e is not None:
            post_user_avatar = avatar_e.find('img').attrs['src']

        post_user_info = e.find('div', class_='post-user-info').get_text().strip()  # text?

        print(post_id, post_user_username, post_user_title, post_user_avatar, post_user_info)

        post_message_e = e.find('div', class_='post_message')

        print(post_message_e.text)


if __name__ == "__main__":
    app()
