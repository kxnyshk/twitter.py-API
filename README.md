# twitter.py-API
Python script for scrapping off and fetching user's data off Twitter using Twitter Developer elevated API via Tweepy modules & Python.

## Fetching the repo
 - Download twitter.py-API [.zip](https://github.com/kxnyshk/twitter.py-API/archive/refs/heads/master.zip)
 - Unzip the folder

## How to use
 - Head to the `./Static/` folder and open the [userVerify.txt](https://github.com/kxnyshk/twitter.py-API/blob/master/Static/userVerify.txt) file.
 - Edit the content of the file (if already written) to the [Twitter username](https://help.twitter.com/en/managing-your-account/twitter-username-rules) you wanna scrape and fetch data off.
 - Now, open the [main.py](https://github.com/kxnyshk/twitter.py-API/blob/master/main.py) file in the terminal of your preferred IDE.

  ### Commands
    Press:
    - `1`: get Home Feed
    - `2`: get User Data
    - `3`: get User Mentions
    - `4`: get User Timeline
    - `5`: get Liked Tweets
    - `6`: get User's Retweeted
    - `7`: search Topic
    - `8`: get Followers (upto 20)
    - `9`: get Following (upto 20)
    - `-1`: System exit
    
## Twitter Dev Auth setup
 - The Twitter Developer Authentication for an elevated API has been done through [here](https://developer.twitter.com/en/products/twitter-api).
 - Read the official documentation [here](https://developer.twitter.com/en/docs)
 - The API & TOKEN [keys](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api#:~:text=API%20Key%20and%20Secret%3A%20Essentially,Tokens%20or%20App%20Access%20Token.) are saved via [configparser](https://docs.python.org/3/library/configparser.html) in Python.
 - Therefore, you would need to setup your own keys after [signing up](https://developer.twitter.com/en/portal/petition/essential/basic-info) for Twitter Dev account.
 - To setup the config path, create this path/file: `./TwitterDev/config.ini` in the dir/zip.
 - No need to re-setup the path in any code, it has already been declared in [auth.py](https://github.com/kxnyshk/twitter.py-API/blob/master/auth.py)

## About Tweepy
 - The requests between the script and the API has been handled through Tweepy module.
 - Read the official documentation [here](https://docs.tweepy.org/en/stable/)
