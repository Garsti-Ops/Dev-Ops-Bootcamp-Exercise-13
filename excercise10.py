import requests

res = requests.get("https://api.github.com/users/Garsti-Ops/repos")

for obj in res.json():
    print(f'Repo-Name: {obj["name"]} Url: {obj["url"]}')