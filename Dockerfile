ARG FUNCTION_DIR="/home/app/"

FROM python:slim-buster

ARG FUNCTION_DIR
RUN mkdir -p ${FUNCTION_DIR}
# COPY *.py ${FUNCTION_DIR}
COPY . ${FUNCTION_DIR}

# Installing Lambda image dependencies
RUN apt-get update \
  && apt-get install -y \
  g++ \
  curl \
  make \
  cmake \
  unzip \
  libcurl4-openssl-dev
# RUN python3 -m pip install awslambdaric

# Installing AWS CLI to upload to S3 bucket
# RUN  pip3 install \
#  awscli
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
    && unzip awscliv2.zip \
    && ./aws/install

# Installing mysqldump and cleaning apt cache
RUN apt update && apt install -y mariadb-client && \
  apt-get clean autoclean && \
  apt-get autoremove --yes && \
  rm -rf /var/lib/{apt,dpkg,cache,log}/

WORKDIR ${FUNCTION_DIR}
RUN chmod +x backupdb
# ENTRYPOINT [ "/usr/local/bin/python3", "-m", "awslambdaric" ]
# CMD [ "main.backup" ]
CMD [ "./backupdb" ]
