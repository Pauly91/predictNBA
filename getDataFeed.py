import base64
import requests


def send_request():
    # Request

    try:
        response = requests.get(
            url={'https://api.mysportsfeeds.com/v1.1/pull/nba/2016-2017-regular/daily_player_stats.csv'},
            params={
                "fordate": "20161121"
            },
            headers={
                "Authorization": "Basic " + base64.b64encode('{}:{}'.format({'poly91'},{'abel1234'}).encode('utf-8')).decode('ascii')
            }
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


def main():
    send_request()

if __name__ == '__main__':
    main()
