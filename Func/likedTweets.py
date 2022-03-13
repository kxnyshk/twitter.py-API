from auth import API


def get_favourites():

    def favourites():

        tweets = API.get_favorites()
        
        for favs in tweets:
            print(f'\n{favs.text}')
    
    def verify():

        print("\nVerificaion for accessing User's liked tweets ..")
        user = input('Username: ')

        with open('./Static/userVerify.txt', 'r') as f:
            
            if f.read() == user:
                favourites()

            else:
                ERR = 'Sorry! Not verified.'
                print(ERR)

    verify()