from dotenv import load_dotenv
import os

print(os.getenv('USER'))
print(os.getenv('PASSWORD'))
print(os.getenv('PORT'))
print(os.getenv('HOST'))
load_dotenv()
print(os.getenv('USER'))
print(os.getenv('PASSWORD'))
print(os.getenv('PORT'))
print(os.getenv('HOST'))

print(os.environ)