#!/bin/bash

echo Closing Sublime ...
killall sublime_text
echo "Copying your config ..."
echo
cp * ~/.config/sublime-text-3/Packages/User/

echo Done!
echo
echo Restart Sublime.
subl &
