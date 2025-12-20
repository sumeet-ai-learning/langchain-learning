import os

from dotenv import load_dotenv

load_dotenv(override=True)

if __name__ == '__main__':
    print('PyCharm')
    print(os.environ.get('OPENAI_API_KEY'))
