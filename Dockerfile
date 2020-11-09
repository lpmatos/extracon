ARG PYTHON_VERSION=3.8-slim

FROM python:${PYTHON_VERSION} as base

FROM base as install-env

COPY [ "requirements.txt", "." ]

RUN apt-get update && apt-get install libcurl4-gnutls-dev librtmp-dev -yq && \
    pip install --upgrade pip && pip install --upgrade setuptools && \
    pip install --user --no-warn-script-location -r ./requirements.txt

FROM base

LABEL maintainer="Lucca Pessoa da Silva Matos - luccapsm@gmail.com" \
        org.label-schema.version="2.0.0" \
        org.label-schema.release-data="06-07-2020" \
        org.label-schema.url="https://github.com/lpmatos" \
        org.label-schema.alpine="https://alpinelinux.org/" \
        org.label-schema.python="https://www.python.org/" \
        org.label-schema.name="Extracon"

RUN apt-get update && \
    apt-get install bash zip -qy && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/code

COPY --from=install-env [ "/root/.local", "/usr/local" ]

COPY [ "./code", "." ]

RUN find ./ -iname "*.py" -type f -exec chmod a+x {} \; -exec echo {} \;;

CMD [ "python", "main.py" ]
