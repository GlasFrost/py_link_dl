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

<url> is the URL starting with "http://" and not containing any spaces.
<comment> explains itself. It should contain at least one word. All chars the console supports as input are allowed.
WARNING: Use this scrit with care! SQL-injection-attacks are possible, just be warned.


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
