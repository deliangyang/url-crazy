# -*-- coding:utf-8 -*--
import os
import re
import sys
import argparse


if __name__ == '__main__':
    ruby = os.popen('which ruby').readline().strip('\n')
    if not re.findall(r'ruby', ruby):
        os.system('yum install ruby -r')

    parse = argparse.ArgumentParser()
    parse.add_argument('url', type=str, default=None, help='url')
    parse.add_argument('--type', type=int, default=1, help='default 1, 1: typo, 2: backward link')
    args = parse.parse_args(sys.argv[1:])
    os.system('chmod +x urlcrazy')
    print('please wait for a moment...')

    pattern = re.compile(r'-{10}')
    split_pattern = re.compile(r'\s{3}')

    if args.type == 1:
        miss_split_line = False
        for line in os.popen('./urlcrazy %s' % args.url).readlines():
            if pattern.findall(line):
                miss_split_line = True
                continue
            if not miss_split_line:
                continue
            print(line)
            # items = split_pattern.split(line)
            # new_arr = []
            # for item in items:
            #     if len(item) > 0:
            #         new_arr.append(item)
            # if new_arr:
            #     print(new_arr[1].strip())
    elif args.type == 2:
        pass
