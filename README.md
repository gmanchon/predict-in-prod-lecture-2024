
## instructions

``` bash
docker build -t taxifare .

docker images

docker run taxifare
docker run -it taxifare /bin/sh

docker container ls

docker stop xxx
docker kill xxx

gcloud artifacts repositories create taxifare-lecture
	--repository-format=docker
	--location=europe-west1
	--description="une description"

docker image tag taxifare $IMAGE_NAME

docker push $IMAGE_NAME

gcloud run deploy --image $IMAGE_NAME --region $REGION
```

## apple silicon

``` bash
docker build -t $IMAGE_NAME:intel --platform linux/amd64 .

docker push $IMAGE_NAME:intel
```
