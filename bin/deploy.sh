#! /bin/bash
CONTAINER_NAME="${CONTAINER_NAME:-twunde764/fib:dev}"
EC2_INSTANCE="${EC2_INSTANCE:-54.224.50.156}"

# build and push the container
docker build -t "$CONTAINER_NAME" .
docker push "$CONTAINER_NAME"
# reboot service. This will automatically pull the latest dev tag of the container.
# If you want to use a different tag, you will need to update the user data script in the automation repo
# WARNIGN: This assumes that you've configured your ssh config to automatically use the SSH key
ssh ec2-user@$EC2_INSTANCE "sudo systemctl restart docker.fib"


