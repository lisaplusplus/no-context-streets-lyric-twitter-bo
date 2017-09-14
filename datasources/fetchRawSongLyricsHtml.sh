#!/bin/bash

HTTP_TOOL="curl"
REMOTE_URL_LIST="songUrlList.txt"
LOCAL_SAVE_TARGET="rawhtml/songhtml/"

which $HTTP_TOOL 1>/dev/null 2>&1
if [[ "$?" -ne 0 ]]
then
  echo "The '$HTTP_TOOL' command couldn't be found. Please install $HTTP_TOOL."
  exit
fi

if [[ ! -e $LOCAL_SAVE_TARGET ]]
then
  mkdir -p $LOCAL_SAVE_TARGET
fi

cat $REMOTE_URL_LIST | while read url; do curl -o "$LOCAL_SAVE_TARGET/$(uuidgen).html" $url; done

if [[ "$?" -eq 0 ]]
then
  echo "$HTTP_TOOL returned a success code."
else
  echo "$HTTP_TOOL failed. See stdout for detals."
fi
