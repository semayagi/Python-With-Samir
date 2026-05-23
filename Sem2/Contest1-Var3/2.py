# {"x": {"y": {"z": 5}}} -> {"x.y.z": 5}
def flatten_dict(data: dict) -> dict:
    result = {}
    for key, value in data.items():
        if isinstance(value, dict):
            for k, v in flatten_dict(value).items(): # Возможно на контесте я здесь забыл .items()
                result[f"{key}.{k}"] = v
        else:
            result[key] = value
    return result

# Проверка

d = {"x": {"y": {"z": 5}}}
d = flatten_dict(d)
print(d)

d = {"x": 2, "a": {"b": 3, "c": 4}}
d = flatten_dict(d)
print(d)