ARG BUILD_FROM
#ARG BUILD_FROM=hassioaddons/base-python:5.2.0
#ARG BUILD_FROM=python:3.6
FROM $BUILD_FROM

# Setup base
#ARG BUILD_ARCH=amd64

# Copy data for add-on
COPY run.sh /
RUN chmod a+x /run.sh
RUN whoami
RUN pwd
RUN ls -al

CMD [ "/run.sh" ]