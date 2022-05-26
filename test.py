from dotenv import load_dotenv, dotenv_values, find_dotenv

load_dotenv()  # take environment variables from .env.

# Code of your application, which uses environment variables (e.g. from `os.environ` or
# `os.getenv`) as if they came from the actual environment.

config = dotenv_values(find_dotenv())

print(config)