#!/bin/bash

# store data in a variable
mesg="Hello World!"

# print to the screen with echo
echo $mesg

# print variable to the screen 2nd method
# echo ${mesg}

echo "Who do you want to say hello to?"

read person

echo Hello ${person}

# for x in {1..25}; do echo "I have ${x} dollars in my pocket"; sleep 2; done
# for x in {1..10}; do echo "interface ${x}"; echo "switch port access vlan 10"; done

echo $1