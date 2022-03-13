# imports
import sys
from Func.homeFeed import home_feed
from Func.userData import user_data
from Func.mentions import mentions
from Func.userTimeline import user_timeline
from Func.likedTweets import get_favourites
from Func.retweeted import get_retweeted
from Func.searching import search
from Func.followers import get_followers
from Func.following import get_following

# main
def main():

    def choice():

        val = input('\n> ')

        match val:
            case '1':
                home_feed()
            case '2':
                user_data()
            case '3':
                mentions()
            case '4':
                user_timeline()
            case '5':
                get_favourites()
            case '6':
                get_retweeted()
            case '7':
                search()
            case '8':
                get_followers()
            case '9':
                get_following()
            case '-1':
                sys.exit()
            case _:
                ERR = 'Invalid Command!'
                print(ERR)

        choice()

    def menu():

        with open('./Static/mainMenu.txt', 'r') as f:
            print(f'\n{f.read()}')

        choice()

    menu()

# test
main()
