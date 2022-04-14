# FYP TTVS Backend Test

This is a Python app to test backend API.

## Startup

To start the test, clone the directory, run the following code.

```{python}
pip3 install -r requirements
```

## Test

This test takes at least 30 minutes. My machine has i3-9100F and 16 GB ram.

The database is deployed at a remote server. A better host machine with a local database may be faster.

Ask the host to provide IP. Modify IP_ADDRESS in testCreateAndUpload.py. Then run the following code.

```{python}
python3 testCreateAndUpload.py
```

## Plot

Then modify the FOLDER_PATH in plot.py

```{python}
python3 plot.py
```

Then you can see the diagram in FOLDER_PATH.

## Sample

Sample result is below:

![Issue Time](./14-04-2022-trial-2/issuing-time-diagram.png)

![Upload Time](./14-04-2022-trial-2/upload-time-diagram.png)