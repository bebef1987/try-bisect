Try-bisect 

This tool will trigger try builds on a seres of commits.

Install:
```
pythoon setup.py install
```

Usage:
```
usage: try_bisect [-h] -g GOOD -b BAD -c COMMAND [-p PATH_TO_REPO]

optional arguments:
  -h, --help            show this help message and exit
  -g GOOD, --good GOOD  last known good rev
  -b BAD, --bad BAD     last known bad rev
  -c COMMAND, --command COMMAND
                        try build command line. See https://mozilla-
                        releng.net/trychooser/
  -p PATH_TO_REPO, --path_to_repo PATH_TO_REPO
                        path to hg repo
```