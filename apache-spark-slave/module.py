from osv.modules import api

api.require('java')

default = api.run("--cwd=/spark /java.so -Xms512m -Xmx512m -cp /spark/conf:/spark/jars/* -Dscala.usejavacp=true org.apache.spark.deploy.worker.Worker 10.10.100.9:7077")


