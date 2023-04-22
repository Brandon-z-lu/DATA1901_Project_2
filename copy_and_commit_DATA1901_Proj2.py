import argparse
import os
import shutil
from sh import git

# Usage
#####################################################################################
# src = os.path.expanduser("~/DATA1901_Project_2")
# dest = os.path.expanduser("~/Uni-Code/4_DATA1901_RStudio/DATA1901_Project_2")


def copy_contents(src, dest):
    if not os.path.exists(dest):
        os.makedirs(dest)

    for item in os.listdir(src):
        if item == '.git':
            continue

        src_path = os.path.join(src, item)
        dest_path = os.path.join(dest, item)

        if os.path.isfile(src_path):
            shutil.copy2(src_path, dest_path)
        elif os.path.isdir(src_path):
            copy_contents(src_path, dest_path)


def commit_changes(path, message):
    os.chdir(path)
    git.add('-A')
    git.commit('-m', message)


def main():
    parser = argparse.ArgumentParser(
        description='Copy contents and commit changes in two directories.')
    parser.add_argument('message', type=str, help='Commit message')

    args = parser.parse_args()
    message = args.message

    # Set the source and destination paths
    #####################################################################################
    src = os.path.expanduser("~/DATA1901_Project_2")
    dest = os.path.expanduser(
        "~/Uni-Code/4_DATA1901_RStudio/DATA1901_Project_2")

    copy_contents(src, dest)
    commit_changes(src, message)
    commit_changes(dest, message)


if __name__ == '__main__':
    main()
