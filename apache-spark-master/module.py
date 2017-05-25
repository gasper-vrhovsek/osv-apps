from osv.modules import api

api.require('java')

default = api.run("--cwd=/spark /java.so -Xms512m -Xmx512m -cp /spark/conf:/spark/jars/* -Dscala.usejavacp=true org.apache.spark.deploy.master.Master 1 --host 127.0.0.1 --port 7077 --webui-port 8080")
# default = api.run("/java.so -Xms512m -Xmx512m -cp /spark/conf:/spark/jars/* -Dscala.usejavacp=true org.apache.spark.deploy.master.Master --host osv.local --port 7077 --webui-port 8080")
