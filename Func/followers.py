from auth import API


def get_followers():

    def followers():

        follower = API.get_followers()
        
        for f in follower:
            print(f'\n{f.screen_name}')
    
    def verify():

        print("\nVerificaion for accessing User's followers ..")
        user = input('Username: ')

        with open('./Static/userVerify.txt', 'r') as f:
            
            if f.read() == user:
                followers()

            else:
                ERR = 'Sorry! Not verified.'
                print(ERR)

    verify()