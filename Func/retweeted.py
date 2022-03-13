from auth import API


def get_retweeted():

    def retweeted():

        rts = API.get_retweets_of_me()
        
        for rt in rts:
            print(f'\n{rt.text}')
    
    def verify():

        print("\nVerificaion for accessing User's retweeted ..")
        user = input('Username: ')

        with open('./Static/userVerify.txt', 'r') as f:
            
            if f.read() == user:
                retweeted()

            else:
                ERR = 'Sorry! Not verified.'
                print(ERR)

    verify()