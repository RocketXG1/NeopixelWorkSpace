def read_config_kv(path="/Recipe/recipe.txt"):
    config = {}
    try:
        with open(path, "r") as file:
            for line in file:
                stripped = line.strip()
                if not stripped or "=" not in stripped:
                    continue
                key, value = stripped.split("=", 1)
                key = key.strip()
                value = value.strip()
                if key:
                    config[key] = value
    except OSError:
        return {}
    return config


def write_config_kv(config, path="/Recipe/recipe.txt"):
    with open(path, "w") as file:
        for key, value in config.items():
            file.write("{}={}\n".format(key, value))
