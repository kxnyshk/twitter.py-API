from auth import API


def mentions():

    def access_mentions():

        mentions_tweets = API.mentions_timeline()
        
        for tweet in mentions_tweets:
            print(f'\n{tweet.text}')
    
    def verify():

        print("\nVerificaion for accessing User's mentions ..")
        user = input('Username: ')

        with open('./Static/userVerify.txt', 'r') as f:
            
            if f.read() == user:
                access_mentions()

            else:
                ERR = 'Sorry! Not verified.'
                print(ERR)

    verify()