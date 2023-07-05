ARG BUILD_FROM
# hadolint ignore=DL3006
FROM ${BUILD_FROM}

# Set shell
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Install requirements for add-on
RUN apk update && apk add --update --no-cache \
	python3 \
	py3-pip && \
	ln -sf python3 /usr/bin/python

# Copy data for add-on
COPY app.py /
COPY run.sh /
COPY requirements.txt /tmp/
# Install requirements for add-on
RUN pip install -r /tmp/requirements.txt

RUN chmod a+x /run.sh
CMD [ "/run.sh" ]