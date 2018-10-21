#!/usr/bin/python

from pathlib import Path


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


symlinks = [
    (Path("root/home/user/.config/awesome"), Path.home().joinpath(Path(".config/awesome")))
]


def create_or_update_symlink(target, link):
    print("Creating " + str(link) + " -> " + str(target))

    try:
        link.parent.mkdir(exist_ok=True, parents=True)
        if link.exists():
            link.unlink()

        link.symlink_to(target.resolve())
    except Exception as exception:
        print(bcolors.FAIL + "Cannot create symlink\n" + str(exception) + bcolors.ENDC)


print("Creating or updating symlinks...")
for target, link in symlinks:
    create_or_update_symlink(target, link)
