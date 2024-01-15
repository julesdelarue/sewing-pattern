FROM gitpod/workspace-full:latest

SHELL ["/bin/bash", "-c"]

RUN sudo apt-get update \
    && sudo apt-get update \
    && sudo apt-get clean
