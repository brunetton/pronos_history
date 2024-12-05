## Install

### Create Docker image

    docker build -t sospronos .

### Run Docker image

    touch results
    docker run -v ./results:/app/results sospronos
