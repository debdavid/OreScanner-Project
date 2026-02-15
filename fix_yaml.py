import yaml
import os

# Point exactly to the local folder created (bypassing iCloud)
train_path = os.path.expanduser("~/datasets/ore_data/images/train")

config_data = {
    "train": train_path,
    "val": train_path,
    "nc": 1,
    "names": ["Iron Ore"]
}

with open("data_config.yaml", "w") as f:
    yaml.dump(config_data, f, sort_keys=False)

print(f"✅ YAML created! Pointing safely to: {train_path}")
