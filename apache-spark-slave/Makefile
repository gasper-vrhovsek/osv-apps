HADOOP_VERSION:=2.7.3
VERSION:=2.1.1
NAME:=spark
DIR:=$(NAME)-$(VERSION)-bin-$(HADOOP_VERSION)
TARBALL:=$(DIR).tgz
URL:=http://d3kbcqa49mib13.cloudfront.net/$(TARBALL)


module: ROOTFS usr.manifest

$(TARBALL):
	wget $(URL)

ROOTFS/$(NAME): $(TARBALL)
	tar xvf $(TARBALL)
	mkdir -p ROOTFS
	mv $(DIR) ROOTFS/$(NAME)
	touch ROOTFS/$(NAME)
	mkdir -p ROOTFS/etc
	touch ROOTFS/etc/javamains
	echo "-cp /spark/conf:/spark/jars/* -Dscala.usejavacp=true org.apache.spark.deploy.worker.Worker 172.16.122.4:7077" > ROOTFS/etc/javamains
	find ./assets/conf -type f -exec cp {} ROOTFS/$(NAME)/conf/. \;
	mkdir -p ROOTFS/$(NAME)/./launcher/target/scala-2.11
	touch ROOTFS/$(NAME)/./launcher/target/scala-2.11/.temp.txt
	echo "temp" > ROOTFS/$(NAME)/./launcher/target/scala-2.11/.temp.txt
	mkdir -p ROOTFS/usr/lib
	cp libOsvProcessBuilder.so ROOTFS/usr/lib/libOsvProcessBuilder.so

usr.manifest:
	echo "/$(NAME)/**: \$${MODULE_DIR}/ROOTFS/$(NAME)/**" >> usr.manifest
	echo "/usr/lib/libOsvProcessBuilder.so: \$${MODULE_DIR}/ROOTFS/usr/lib/libOsvProcessBuilder.so" >> usr.manifest

clean:
	rm -rf ROOTFS $(DIR)
	rm -f usr.manifest $(TARBALL)

ROOTFS: ROOTFS/$(NAME)
