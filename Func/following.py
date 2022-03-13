from auth import API


def get_following():

    def followings():

        following = API.get_friends()
        
        for f in following:
            print(f'\n{f.screen_name}')
    
    def verify():

        print("\nVerificaion for accessing User's following ..")
        user = input('Username: ')

        with open('./Static/userVerify.txt', 'r') as f:
            
            if f.read() == user:
                followings()

            else:
                ERR = 'Sorry! Not verified.'
                print(ERR)

    verify()