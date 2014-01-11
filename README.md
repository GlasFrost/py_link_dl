py_link_dl
==========

This Python script downloads the HTML-Code of a website and puts it into a SQLite3-Database. The URL and a timestamp are saved, too. You can give a comment to every entry, but that is optional.

I created this script "quick and dirty", so feel free to improve the code.

Usage:
------
You use it in the command line:

```bash
  cd /path/to/script/
  ./link_dl.py <url> <comment>
```

```<url>``` is the URL starting with "http://" or "https://" and not containing any spaces.

```<comment>``` explains itself. It should contain at least one word. All chars the console supports as input are allowed.

WARNING: Use this script with care! SQL-injection-attacks are possible, just be warned.

"Did it work?"
--------------
There can be different things printed to the command line.

```[SUC]``` indicates success.

```[WRN]``` indicates an error that didn't cause the code to stop.

```[ERR]``` indicates an error that caused the script to stop.

It also says which class (in this case always "link_dl") and which function caused the message and of course it says what happened.

If the script comes successfully to an end without an error, it says:

```[SUC] link_dl.insert(): Done```

The other messages explain themselves.

Example:
--------
```./link_dl.py http://example.com This is a comment```

The following data will be stored in the SQLite3-file:
- an *ID*, each entry gets its own
- the *url*, in this example it's "http://example.org"
- the *HTML-Code* of the website (but no additional files)
- the current *timestamp*

If the database file doesn't exist, it is created.

License:
--------

This piece of software is licensed under the terms of The MIT License.
See the ```LICENSE``` file for more info.
