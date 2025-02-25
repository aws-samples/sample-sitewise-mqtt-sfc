sitewise-mqtt-sfc
=================

Use an MQTT-enabled AWS IoT Sitewise gateway to send data from various industrial equipment, using [SFC](https://github.com/aws-samples/shopfloor-connectivity), to Sitewise Service in the cloud.

```sh
               +------------------MQTT-enabled-Sitewise-Gateway------+                    
               |  SFC   VTL                                          |                    
               |  CONF  CONF                                         |                    
               |   |     |                                           |                    
               | +-+-----+--+     +-------------+     +-----------+  |                    
               | |          |     |             |     |           +--+--> AWS IoT Sitewise
MODBUS-TCP ----+-+   SFC    +-----> MQTT Broker +-----> Publisher |  |                    
DEVICE         | |          |     |             |     |           +--+--> Amazon S3       
               | +----------+     +-------------+     +-----------+  |                    
               |                                                     |                    
               |                                                     |                    
               +-----------------------------------------------------+                     
```

<br>
<br>
<br>

> The following steps require you to have a running v3 MQTT-enabled AWS IoT Sitewise Gateway. Please use 


#### **Step 1**: Login to SW Gateway and clone Repo

- login to your v3 MQTT-enabled Sitewise Gateway
- fyi check the running containers: run `docker ps` - you should see the emqx container bound to port 1883 (that is the mqtt port where we will send data later)
- clone that repo:

```sh
git clone https://github.com/aws-samples/sample-sitewise-mqtt-sfc.git
```

#### **Step 2**: Run Modbus simulator

- modbus simulation will be started at port `502`
- make sure to have the program running detached from your current shell using e.g. `screen`

```sh
cd modbus
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python modbus-server.py
```

#### **Step 3**: Install SFC

We're using ready to use kotlin SFC binary modules, available as [tar.gz from github](https://github.com/aws-samples/shopfloor-connectivity/releases)
- [`sfc-main`](https://github.com/aws-samples/shopfloor-connectivity/blob/mainline/docs/core/sfc-configuration.md) - the core module, receiving config and all the source/target mapping
- [`mqtt-target`](https://github.com/aws-samples/shopfloor-connectivity/blob/mainline/docs/adapters/mqtt.md) - generic mqtt adapter, to send data to mqtt broker topics
- [`debug-target`](https://github.com/aws-samples/shopfloor-connectivity/blob/mainline/docs/targets/debug.md) - inspect the [SFC-Output](https://github.com/aws-samples/shopfloor-connectivity/blob/mainline/docs/sfc-data-format.md) in stdout
- [`modbus-tcp`](https://github.com/aws-samples/shopfloor-connectivity/blob/mainline/docs/adapters/modbus.md) - adapter, to read from modbus devices

```sh
#cd ..
cd sfc
./install.sh # that script downloads all reuqired modules from github...
```

#### **Step 4**: Inspect teh SFC config and Velocity Template



#### **Step 5**: Run SFC

```sh
# cd sfc
cat run.sh
# export SFC_DEPLOYMENT_DIR=$(pwd)
# sfc-main/bin/sfc-main -config sfc-config.json -info
./run.sh
./run.sh
2025-02-25 16:36:33.27  INFO  - Creating configuration provider of type ConfigProvider
2025-02-25 16:36:33.38  INFO  - Waiting for configuration
2025-02-25 16:36:33.55  INFO  - Sending initial configuration from file "sfc-config.json"
2025-02-25 16:36:33.999 INFO  - Received configuration data from config provider
2025-02-25 16:36:34.01  INFO  - Waiting for configuration
2025-02-25 16:36:34.02  INFO  - Creating and starting new service instance
2025-02-25 16:36:34.101 INFO  - Created instance of service MainControllerService
2025-02-25 16:36:34.102 INFO  - Running service instance
2025-02-25 16:36:34.103 INFO  - Creating an in-process reader for adapter "ModbusAdapter" of protocol adapter type MODBUS-TCP
2025-02-25 16:36:34.161 INFO  - SFC_MODULE MODBUS-TCP: VERSION=1.0.0, MODBUS_VERSION=1.0.0, SFC_CORE_VERSION=1.8.1, SFC_IPC_VERSION=1.8.1, BUILD_DATE=2025-02-14
2025-02-25 16:36:34.165 INFO  - Creating in process target writer for target ID swMqttTarget
2025-02-25 16:36:34.259 INFO  - SFC_MODULE MQTT-TARGET: VERSION=1.0.0, SFC_CORE_VERSION=V1.8.2, SFC_IPC_VERSION=V1.8.2, BUILD_DATE=2025-02-24
2025-02-25 16:36:34.261 INFO  - MQTT Writer for target "swMqttTarget" writer publishing to topics at endpoint tcp://localhost on target swMqttTarget
2025-02-25 16:36:34.265 INFO  - No adapter or target metrics are collected
2025-02-25 16:36:34.307 INFO  - Connected to localhost:502
```




