import pandas as pd

df = pd.DataFrame(
    {
        "env": ["tuple", "typeddict", "explicitrange", "dataclass"],
        "module": [
            "time_get_range_startlength",
            "time_get_range_startstop",
            "time_get_range_typeddict",
            "time_get_range_dataclass",
        ],
    }
)

n = 20
shuffled = pd.concat([df.sample(frac=1) for x in range(n)])

with open("run-benchmarks.sh", "a") as f:
    f.write("hatch env run --env tuple python create_store.py\n")
    for index, row in shuffled.iterrows():
        f.write(f"hatch env run --env {row['env']} python {row["module"]}.py\n")
