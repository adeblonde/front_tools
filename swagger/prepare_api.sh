#!/bin/bash

source ../../user_setenv.sh

export SCENARIO_NAME="server_swagger"
export SCENARIO_DIR=$CODE_DIR/front_tools/$SCENARIO_NAME

if [ ! -f $SCENARIO_DIR ]
then
	mkdir -p $SCENARIO_DIR
fi

cd $SCENARIO_DIR

export SWAGGER_FILE=$SCENARIO_DIR/"swagger.yml"
export API_SERVER_FOLDER=$SCENARIO_DIR/api
export API_CLIENT_FOLDER=$SCENARIO_DIR/client
export API_CLIENT_LANGUAGE="python"
export API_SERVER_LANGUAGE="python-flask"

if [ ! -f $API_CLIENT_FOLDER ]
then
	mkdir -p $API_CLIENT_FOLDER
fi
if [ ! -f $API_SERVER_FOLDER ]
then
	mkdir -p $API_SERVER_FOLDER
fi

### install maven & java
# sudo apt-get install openjdk-8-jdk maven javacc openjdk-8-jdk-headless python3-pip
# sudo pip3 install setuptools

### download swagger codegen
wget http://central.maven.org/maven2/io/swagger/swagger-codegen-cli/2.3.1/swagger-codegen-cli-2.3.1.jar -O swagger-codegen-cli.jar
export SWAGGER_BIN=swagger-codegen-cli.jar

### set swagger file
$CODE_DIR/front_tools/swagger/set_openapi.sh $CODE_DIR/front_tools/swagger/swagger.yml $SWAGGER_FILE

### run codegen on swagger.json
echo $SWAGGER_BIN
java -jar $SWAGGER_BIN generate \
   -i $SWAGGER_FILE \
   -l $API_SERVER_LANGUAGE \
   -o $API_SERVER_FOLDER

### convert spaces to tabs
for python_file in $(find $API_SERVER_FOLDER -name '*.py')
do
	echo $python_file
	sed -i 's#    #	#g' $python_file
done