import yaml
with open("yaml_data.yaml","r",encoding="utf-8") as f:
    data=yaml.load(f,Loader=yaml.FullLoader)
    print(data)

