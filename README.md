# Tsuku

Tsuku is a simple cli tool made in python, 
its whole purpose is to be able to write and save a minimal list.

This project is developed on mac for mac, for bash and zsh,
since those are the terminals i use and the platform i use daily.


If anyone is intrested, i highly advise configuring it to your liking.

Commands:

`l` lists all the tasks

`c` is for create, example `c newitem` 

`r` is for remove, asks for input, 
prints curr list and asks for either index or item name to delete it and shows new list



How to run

to run the project i used the python3 interpreter, and to setup a simple global custom command i added a simlpe one line function to my .bash_profile
`
function t(){
  python3 {path}/tsuku/tsuku.py $1 $2 $3 
}
`
i only added 3 args cause i mostly write one or two words, in the setup file i added, it gives you more which is enough to write a sentence if thats how you wanna use it.

The items are all stored in a data.txt file that should be located in the same dir as the tsuku.py file. If you want to quickly empty the list or modify it, all items are separted by a `|`

I inittially used argparse but tbh for such a simple tool that i wanted to make with as little outside tooling as possible, i just used pythons built in sys.argv.

I am quite happy with the result of this little cli tool, more over this gave me a good reason to learn the very basics of python and how to use it. Biggest thing i had to get use to is not using ++ and instead +=. 
