import os

import yaml


with open("config.yaml", "r", encoding="utf-8") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
if not os.path.exists(config["path"]):
    os.makedirs(config["path"])

config = config