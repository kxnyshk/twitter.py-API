from auth import API


def home_feed():

    def access_feed():

        public_tweets = API.home_timeline()
        
        for tweet in public_tweets:
            print(f'\n{tweet.text}')
    
    def verify():

        print("\nVerificaion for accessing User's home feed ..")
        user = input('Username: ')

        with open('./Static/userVerify.txt', 'r') as f:
            
            if f.read() == user:
                access_feed()

            else:
                ERR = 'Sorry! Not verified.'
                print(ERR)

    verify()