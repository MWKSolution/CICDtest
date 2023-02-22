"""Sample program that does nothing special to test CICD pipline."""
import os
from dotenv import load_dotenv
from yaml import safe_load
from package.functions import function


load_dotenv()
LOGIN = os.environ.get("LOGIN")
PASSWD = os.environ.get("PASSWD")

if __name__ == "__main__":
    print("Hello CICD")
    print(function(1, 2))
    print(LOGIN, PASSWD)
    with open(".pre-commit-config.yaml", encoding="utf-8") as yaml_file:
        data = safe_load(yaml_file)

    for r in data["repos"]:
        print(r["hooks"][0]["id"])
