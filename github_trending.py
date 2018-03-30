import requests
from datetime import datetime, timedelta


def get_date_days_ago(days_number):
    date_days_ago = datetime.now() - timedelta(days=days_number)
    return date_days_ago


def get_trending_repositories(date_start_search, top_size):
    params_repo_search = {
        'q': 'created:>{}'.format(date_start_search),
        'sort': 'star'
    }
    response = requests.get(
        'https://api.github.com/search/repositories',
        params=params_repo_search
    )
    repositories = response.json()['items']
    return repositories[:top_size]


def get_open_issues_amount(repo_owner, repo_name):
    response = requests.get(
        'https://api.github.com/repos/{}/{}/issues'.format(
            repo_owner,
            repo_name
        )
    )
    open_issues = response.json()

    return len(open_issues)


if __name__ == '__main__':
    date_start = get_date_days_ago(days_number=7)
    date_search_format = datetime.strftime(
        date_start,
        '%Y-%m-%dT%H:%M'
    )

    try:
        trending_repositories = get_trending_repositories(
            date_search_format,
            top_size=20
        )

        for index, repo in enumerate(trending_repositories, start=1):
            issues_amount = get_open_issues_amount(
                repo['owner']['login'],
                repo['name']
            )
            print('{:>2}: {:<30} stars={:<4}   открыто issues={:<2}   {}'.format(
                index,
                repo['name'],
                repo['stargazers_count'],
                issues_amount,
                repo['html_url']
            ))
    except requests.ConnectionError:
        exit('Не удалось подключится к github.com')
