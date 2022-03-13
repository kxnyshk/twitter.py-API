from auth import API


def search():

    def search_():

        t = input('\nQuery: ')
        q = f'{t}'
        searches = API.search_tweets(q)
        
        for s in searches:
            print(f'\n{s.text}')
    
    def verify():

        print("\nVerificaion for searching ..")
        user = input('Username: ')

        with open('./Static/userVerify.txt', 'r') as f:
            
            if f.read() == user:
                search_()

            else:
                ERR = 'Sorry! Not verified.'
                print(ERR)

    verify()