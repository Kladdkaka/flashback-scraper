import sys
import time
from typing import List

import typer
import requests
from bs4 import BeautifulSoup, Tag
from fake_useragent import UserAgent
from pathlib import Path
import json

app = typer.Typer()


@app.command()
def thread(thread_id: int, output_path: str = None, user_agent: str = None, sleep_ms: float = 0.5):
    typer.echo(f"scrape thread: {thread_id}")

    scraped_pages = set()
    scraped_posts = set()

    if user_agent is None:
        user_agent = UserAgent().chrome

    if output_path is not None:
        p = Path(output_path)

        if p.exists():
            with open(p, 'r', encoding='utf-8') as f:
                for line in f:
                    data = json.loads(line)

                    scraped_pages.add(data['page_id'])
                    scraped_posts.add(data['post_id'])
        else:
            open(p, 'a').close()

    handle = open(Path(output_path), 'a', encoding='utf-8') if output_path is not None else sys.stdout

    headers = {'User-Agent': user_agent}

    last_page_id = fetch_last_page_id(thread_id, headers)

    print(last_page_id)

    start_page = max(scraped_pages) if len(scraped_pages) > 0 else 1

    for page_id in range(start_page, last_page_id + 1):
        print(f'{page_id}/{last_page_id}')

        post_results = scrape_thread_page(thread_id, page_id, headers)

        # print(post_results)

        for post in post_results:
            if post['post_id'] not in scraped_posts:
                handle.write(json.dumps(post, ensure_ascii=False) + '\n')

            scraped_posts.add(post['post_id'])

        scraped_pages.add(page_id)

        time.sleep(sleep_ms)

    if handle is not sys.stdout:
        handle.close()


def scrape_thread_page(thread_id: int, page_id: int, headers: dict) -> List[dict]:
    r = fetch_thread_page(thread_id, page_id, headers)
    soup = BeautifulSoup(r.content, features='lxml')
    results = []
    # Actually a ResultSet but who cares
    post_elements: List[Tag] = soup.find('div', id='posts').find_all('div', class_='post')
    for e in post_elements:
        post_id = e.attrs['data-postid']

        username = e.find('a', class_='post-user-username').text.strip()
        user_title = e.find('div', class_='post-user-title').text.strip()
        avatar_url = None

        avatar_e = e.find('div', class_='post-user-avatar')
        if avatar_e is not None:
            avatar_url = avatar_e.find('img').attrs['src']

        user_info = e.find('div', class_='post-user-info').get_text().strip()  # text?

        # print(post_id, username, user_title, avatar_url, user_info)

        post_message_e = e.find('div', class_='post_message')

        # print(post_message_e.text)

        message = post_message_e.text.strip()

        results.append(
            dict(
                thread_id=thread_id,
                page_id=page_id,
                post_id=post_id,
                username=username,
                user_title=user_title,
                avatar_url=avatar_url,
                user_info=user_info,
                message=message
            )
        )

    return results


def fetch_last_page_id(thread_id: int, headers: dict) -> int:
    r = fetch_thread_page(thread_id, 1, headers)

    soup = BeautifulSoup(r.content, features='lxml')
    last_page_id = int(soup.find('span', class_='input-page-jump').attrs['data-total-pages'])

    return last_page_id


def fetch_thread_page(thread_id: int, page_id: int, headers: dict) -> requests.Response:
    return requests.get(f'https://www.flashback.org/t{thread_id}p{page_id}', headers=headers)


if __name__ == "__main__":
    app()
