"""Tool for getting crumb data from Jenkins."""
import os
from requests import get, exceptions
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()
JENKINS_URL = os.environ.get("JENKINS_URL", default="")
JENKINS_LOGIN = os.environ.get("JENKINS_LOGIN", default="")
JENKINS_PASSWD = os.environ.get("JENKINS_PASSWD", default="")


def get_crumb_data_for_pycharm(jenkins_url: str, jenkins_login: str, jenkins_passwd: str) -> str:
    """Use GET to get crumb data."""
    auth = HTTPBasicAuth(jenkins_login, jenkins_passwd)
    params = {"tree": "crumb"}
    jenkins_path = "/".join(["http:/", jenkins_url, "crumbIssuer/api/json"])
    print("Getting from:", jenkins_path)
    try:
        response = get(jenkins_path, auth=auth, params=params)
        response.raise_for_status()
        crumb_data = response.json()["crumb"]
    except exceptions.HTTPError:
        # noinspection PyUnboundLocalVariable
        return f"{response.status_code} {response.content.decode()}"
    except exceptions.RequestException as error:
        return f"{error}"
    except KeyError as error:
        return f"{error}"

    return crumb_data


if __name__ == "__main__":
    crumb = get_crumb_data_for_pycharm(JENKINS_URL, JENKINS_LOGIN, JENKINS_PASSWD)
    print("Crumb data:", crumb)
