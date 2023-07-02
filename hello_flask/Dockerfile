ARG BUILD_FROM=javata/hassio_flask:test
# hadolint ignore=DL3006
FROM ${BUILD_FROM}

# Set shell
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Copy data for add-on
COPY run.sh /
COPY requirements.txt /tmp/
# Install requirements for add-on
# RUN pip install -r /tmp/requirements.txt

RUN chmod a+x /run.sh
CMD [ "/run.sh" ]