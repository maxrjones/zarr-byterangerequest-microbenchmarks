# Zarr ByteRangeRequest microbenchmarks


-----

## Create benchmarks

```
python create_run.py
```

## Run microbenchmarks

```
bash run-benchmarks.sh
```

## Plot results

```
hatch env run --env analysis papermill plot-results.ipynb results.ipynb
```

## License

`zarr-byterangerequest-microbenchmarks` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.