import subprocess
import hglib
import os
import signal
import sys
from cmdline import parse_args

class TryBisect():

    def __init__(self):
        # parse arguments
        args = parse_args()
        print args

        #generate path to hg repo
        self.path_to_repo = ""

        if args.path_to_repo and os.path.exists(args.path_to_repo):
            if os.path.exists(os.path.join(self.args.path_to_repo, ".hg")):
                self.path_to_repo = args.path_to_repo
            else:
                raise Exception("Path to Hg repo is not valid!!")

        self.command_line = args.command.split()

        self.good = args.good
        self.bad = args.bad

    def main(self):
        try:
            self.client = hglib.open(self.path_to_repo)
        except:
            raise Exception("Not a valid HG repo")

        repo_root = self.client.rawcommand(['root']).rstrip()
        mach_path = os.path.join(repo_root, "mach")

        commits = self.client.log("%s:%s" %(self.good, self.bad))
        commits.reverse()

        for commit in commits:
            print "%s %s %s" %(commit.node, commit.author, commit.desc.split('\n')[0])

        for commit in commits:
            self.client.update(rev=commit.node, check=True)
            current_commit = self.client.identify().rstrip()

            run_on_try_arg = ["python", mach_path] + self.command_line

            print "Running for commit %s" % current_commit
            print "Running command: %s \n" % run_on_try_arg
            # subprocess.check_output(run_on_try_arg).splitlines()

def main():
    try_bisect = TryBisect()
    try_bisect.main()

if __name__ == "__main__":
    main()