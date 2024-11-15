FROM ubuntu:20.04
ARG DEBIAN_FRONTEND=noninteractive
COPY . /home
WORKDIR /home
RUN apt-get update && \
    apt-get install -y \
    python3 \
    python3-pip \
    ffmpeg \
    libsm6 \
    libxext6 \
    wget
RUN pip install -r requirements.txt
RUN wget https://storage.googleapis.com/tf_model_garden/vision/movinet/movinet_a1_stream.tar.gz -O movinet_a1_stream.tar.gz -q
RUN tar -xvf movinet_a1_stream.tar.gz && rm movinet_a1_stream.tar.gz

