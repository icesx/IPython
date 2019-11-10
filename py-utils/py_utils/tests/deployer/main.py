# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
import argparse

from deployer.deploy import Deploy


def help():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('local_dirs', metavar='local_dirs', type=str, nargs='+',
                        help='local dir to deploy')
    parser.add_argument('--remote_dir', dest='remote_dir', nargs=1,
                        help='the remove target path as /home/mine/workspace')
    parser.add_argument('--password', dest='password', nargs=1,
                        help='password for user on host')
    parser.add_argument('--user', dest='user', nargs=1,
                        help='user fro host')
    parser.add_argument('--host', dest='host', nargs=1,
                        help='ip or hostname')
    args = parser.parse_args()
    return vars(args)


if __name__ == '__main__':
    args = help()
    print(args)
    dirs=args.get('local_dirs')
    for local_dir in dirs:
        deploy = Deploy(local_dir, host=args.get('host')[0], remote_dir=args.get('remote_dir')[0],
                    user=args.get('user')[0], password=args.get('password')[0])
        deploy.zip().scp_file().ssh_unzip()
