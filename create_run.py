import pandas as pd

df = pd.DataFrame(
    {
        "env": ["tuple", "dataclass-if", "dataclass-match"],
    }
)
n = 10

with open("run-benchmarks.sh", "w") as f:
    for method in ["get_range", "get_suffix", "get_offset"]:
        df_method = df
        df_method["method"] = method
        shuffled = pd.concat([df_method.sample(frac=1) for x in range(n)])
        f.write("hatch env run --env tuple python create_store.py\n")
        for index, row in shuffled.iterrows():
            f.write(
                f"hatch env run --env {row['env']} python time_get_{row["env"].replace("-match", "").replace("-if", "")}.py {row["method"]}\n"
            )
