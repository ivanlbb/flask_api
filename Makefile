all: del-container del-image build run	

build:
	docker build -t poc-image:0.0.1 .
run:
	docker run --name poc-container -p 8080:8080 poc-image:0.0.1
run_werkzeug:
	docker run --name poc-container -p 7002:7002 poc-image:0.0.1
exec:
	docker container exec -it poc-container /bin/sh	
logs:
	docker container logs poc-container
del-image:
	docker rmi poc-image:0.0.1
del-container:
	docker rm poc-image
	
delete: del-container del-image
  
