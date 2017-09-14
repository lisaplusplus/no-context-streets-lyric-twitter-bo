#!/bin/bash

HTTP_TOOL="curl"
REMOTE_SONG_HTML_URL="http://www.metrolyrics.com/streets-lyrics.html"
LOCAL_SAVE_TARGET="rawhtml/songlist.html"

which $HTTP_TOOL 1>/dev/null 2>&1
if [[ "$?" -ne 0 ]]
then
  echo "The '$HTTP_TOOL' command couldn't be found. Please install $HTTP_TOOL."
  exit
fi

eval "$HTTP_TOOL -o $LOCAL_SAVE_TARGET $REMOTE_SONG_HTML_URL"

if [[ "$?" -eq 0 ]]
then
  echo "$HTTP_TOOL returned a success code."
else
  echo "$HTTP_TOOL failed. See stdout for detals."
fi

