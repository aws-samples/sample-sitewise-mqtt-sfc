export VERSION="v1.8.3"
export SFC_DEPLOYMENT_DIR=$(pwd)

wget https://github.com/aws-samples/shopfloor-connectivity/releases/download/$VERSION/\
{mqtt-target,debug-target,modbus-tcp,sfc-main}.tar.gz

for file in *.tar.gz; do
  tar -xf "$file"
  rm "$file"
done