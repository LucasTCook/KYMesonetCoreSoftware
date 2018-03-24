echo -n "Do you like pie (y/n)? "
read answer
if echo "$answer" | grep -iq "^y" ;then
    echo Yes
else
    echo No
fi