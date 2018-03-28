import requests
from datetime import datetime, timedelta

API_GITHUB = 'https://api.github.com'


def get_date_for_git_api():
    date_search = datetime.now() - timedelta(days=7)
    date_for_git = datetime.strftime(date_search, '%Y-%m-%dT%H:%M')
    return date_for_git


def get_trending_repositories(date_start_search, top_size):
    response = requests.get(
        '{}/search/repositories?q=created:>{}&sort=star'.format(
            API_GITHUB,
            date_start_search
        )
    )

    for item in range(top_size):
        repository = response.json()['items'][item]
        yield {
            'repo_owner': repository['owner']['login'],
            'repo_name': repository['name'],
            'stars': repository['stargazers_count'],
            'repo_url': repository['html_url']
        }


def get_open_issues_amount(repo_owner, repo_name):
    response = requests.get('{}/repos/{}/{}/issues'.format(
        API_GITHUB,
        repo_owner,
        repo_name
    ))
    open_issues = response.json()

    return len(open_issues)


if __name__ == '__main__':
    date_start = get_date_for_git_api()
    try:
        trending_repositories = get_trending_repositories(
            date_start,
            top_size=20
        )

        for index, repo in enumerate(trending_repositories, start=1):
            issues_amount = get_open_issues_amount(
                repo['repo_owner'],
                repo['repo_name']
            )
            print('{:>2}: {:<30} stars={:<4}   открыто issues={:<2}   {}'.format(
                index,
                repo['repo_name'],
                repo['stars'],
                issues_amount,
                repo['repo_url']
            ))
    except requests.ConnectionError:
        exit('Не удалось подключится к github.com')
