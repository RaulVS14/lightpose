# Office Simulator

## Install

```
conda create --name junction python=3.6
conda activate junction
pip install Flask==1.1.1
```

## Run

```
conda activate junction
python main.py
```

## Change the light power

Example: 

* Room ID: r103
* Power: 80
```
http://127.0.0.1:5000/update/power?id=r103&power=80
```

* Room ID: m101
* Power: 0
```
http://127.0.0.1:5000/update/power?id=m101&power=0
```
