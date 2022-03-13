from auth import API


def user_data():

    def access_data(username):

        user = API.get_user(screen_name=username)

        def print_details(userDict):

            print('\n')
            for keys, values in userDict.items():
                if keys == 'Name' or keys == 'Links' or keys == 'Liked' or keys == 'Tweets':
                    print(f'{keys}:\t\t{values[0]}')
                else:
                    print(f'{keys}:\t{values[0]}')

        
        def user_details():

            userDict = {}

            userDict['Name'] = [f'{user.name}']
            userDict['Username'] = [f'{user.screen_name}']
            userDict['Location'] = [f'{user.location}']
            userDict['Description'] = [f'{user.description}']
            userDict['Links'] = [f'{user.url}']
            userDict['Protected'] = [f'{user.protected}']
            userDict['Followers'] = [f'{user.followers_count}']
            userDict['Following'] = [f'{user.friends_count}']
            userDict['Created'] = [f'{user.created_at}']
            userDict['Liked'] = [f'{user.favourites_count}']
            userDict['Verified'] = [f'{user.verified}']
            userDict['Tweets'] = [f'{user.statuses_count}']

            print_details(userDict)

        user_details()

    def verify():

        print('\nVerificaion for accessing User data ..')
        user = input('Username: ')

        with open('./Static/userVerify.txt', 'r') as f:
            
            if f.read() == user:
                access_data(user)

            else:
                ERR = 'Sorry! Not verified.'
                print(ERR)

    verify()
