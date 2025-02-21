## Local modbus Simulator

### create & activate venv

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### run modbus server

```sh
(.venv) python modbus-server.py

#
# OUTPUT
#
reading file
preparing the storage
Modbus TCP Server is running and updating registers over time...
1 [25]
2 [0]
3 [85]
4 [19]
5 [0]
6 [0]
7 [18233]
8 [0]
9 [4]
Updated Modbus registers
...
```