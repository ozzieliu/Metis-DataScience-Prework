# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > 1. `grep` - grep lets you search for text within a file. This is useful to quickly find strings that you want to view or edit.
> > 2. `man` - displays the help information for the command. Especially helpful when looking up parameters.
> > 3. `touch` - touch creates a new empty file very quickly. This can be used to create files in preparation to storing data.
> > 4. `less` - prints out the file text but in a interactive way instead of dumping everything with `cat`.
> > 5. `rm` - removes files or directories.
> > 6. `pushd` and `popd` - this is new to me. This lets you jump between directories very quickly.
> > 7. `env` - prints out environment settings. Useful for viewing environment settings to check or to update.
> > 8. `ls` - lists the file contents in the directory.
> > 9. `chmod` - change permission on files. This is used very often to set permissions.
> > 10. `sudo` - allow super user operation in certain tasks that may be locked to normal user level.

---


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

> > ls lists all the files in the current directory.
> >
> > `ls -a` lists all the files, including hidden files
> > `ls -l` lists all files in long format with additional information
> > `ls -lh` lists all the files in long format and prints the file sizes in human readable format with KB or MB units.
> >
> > Using a combination of `ls -alh` would be meaningful as it shows me all the files in the directory with additional information such as permission, suffix, created date, and fize size in a human readable format.

---


---

What does `xargs` do? Give an example of how to use it.

> > `xargs` is used to run arguments, especially with commands that can't take long argument strings such as `rm` or `cp`. 
> > For example: If I want to search for all the R Markdown files for deletion in the current directory, I can use xargs in conjuction with find:
> > `find . -name "*.rmd" | xargs rm`

---

