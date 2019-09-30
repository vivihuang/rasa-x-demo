#!/bin/bash

set -Eeuo pipefail

function print_help {
    echo "Available options:"
    echo " start  - Start Rasa Action Server"
    echo " help   - Print this help"
    echo " run    - Run an arbitrary command inside the container"
    echo " run-x  - Run rasa x in container"
}

case ${1} in
    start)
        exec python -m rasa_sdk "${@:2}"
        ;;
    run)
        exec "${@:2}"
        ;;
    run-x)
        exec rasa x "${@:2}"
        ;;
    *)
        print_help
        ;;
esac