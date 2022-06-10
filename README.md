# <img src="https://i.imgur.com/fouiwkc.png" width="40"/> HoneyGain auto daily reward claim
A small and simple python script that will request every day automatically the daily rewards.

## How to use
First, install depedencies with 
``pip install -r requirements.txt`` 
Then, put your environement variables in the .env file.
|||
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HONEYGAIN_TOKEN | Your honeygain API token. (To get it, go in the dev console on HoneyGain's dashboard, and look for any API call. Then, look in the request headers, and look for Authorization. Copy the string after Bearer.) |
| PUSHBULLET_KEY  | Required only for "with_pushbullet.py". It will notify you when you earn your daily reward, with the amount of credits. (To get it, https://www.pushbullet.com/#settings/account -> Create Access Token)       |

Then, set-up a cron job running every hour (as the default claim time can depend on your timezone)
``* * * * * /path/to/honeygain.py`` or you can use the PushBullet script ``* * * * * /path/to/with_pushbullet.py``
And voilà! It will run and automatically claim
