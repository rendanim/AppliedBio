#!/bin/sh

# Directory we run from: blah/gendist.app/Contents/MacOS
mydir=`dirname "$0"`

# Extra quoting required because $dirname may have spaces and double-quotes get
# eaten below.

scriptcmd="cd \\\"${mydir}/../../..\\\" ; \\\"${mydir}/gendist\\\" ; exit"
osascript \
-e 'tell application "Terminal"' \
-e 'activate' \
-e "do script \"$scriptcmd\"" \
-e 'set background color of window 1 to {52224, 65535, 65535}' \
-e 'set normal text color of window 1 to "black"' \
-e 'set cursor color of window 1 to "black"' \
-e 'set custom title of window 1 to "gendist"' \
-e 'end tell'


