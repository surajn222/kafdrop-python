.PHONY: run-app
run-app:
	-echo "Running"
	-python app.py

.PHONY: build
build:
	-echo "Nothing to build"

.PHONY: setup-local-kafka
setup-local-kafka:
	-rm -rf /tmp/vagrant-boxes/
	-cd /tmp && git clone https://github.com/surajn222/vagrant-boxes.git
	-cd /tmp/vagrant-boxes/Ubuntu-kafdrop && make run-docker-kafka

.PHONY: stop-local-kafka
stop-local-kafka:
	-cd /tmp/vagrant-boxes/Ubuntu-kafdrop && make stop-docker-kafka



