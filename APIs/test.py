import openai
import openai.error



def chek_open_api_key(apikey):
    openai.api_key = apikey
    try:
        openai.Model.list()
        print('Valid open-ai key')
        return True
    except openai.error.AuthenticationError:
        print('Invalid open api key')
        return False
    except openai.error.RateLimitError:
        print('Open ai key is valid but exceeds rate limits rate limits or lack sufficient credits')
        return True
    except Exception as e:
        print('An error occureed: {e}')
        return False
    
api_key = ""

chek_open_api_key(api_key)