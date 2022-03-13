from auth import API


def user_timeline():

    def access_user_timeline():

        timeline = API.user_timeline()
        
        for tweet in timeline:
            print(f'\n{tweet.text}')
    
    def verify():

        print('\nVerificaion for accessing User timeline ..')
        user = input('Username: ')

        with open('./Static/userVerify.txt', 'r') as f:
            
            if f.read() == user:
                access_user_timeline()

            else:
                ERR = 'Sorry! Not verified.'
                print(ERR)

    verify()