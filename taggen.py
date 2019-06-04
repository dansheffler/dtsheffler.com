#!/usr/bin/env python

'''
tag_generator.py
Copyright 2017 Long Qian
Contact: lqian8@jhu.edu
This script creates tags for your Jekyll blog hosted by Github page.
No plugins required.
'''

import glob
import os

post_dir = '_posts/'
tag_dir = 'tags/'

filenames = glob.glob(post_dir + '*md')

total_tags = []
for filename in filenames:
    f = open(filename, 'r', encoding="utf8")
    crawl = False
    for line in f:
        if crawl:
            if line.startswith('tags: '):
                line = line[6:]
                line = line.strip()
                line = line.strip("[]")
                current_tags = line.strip().split(", ")
                total_tags.extend(current_tags)
                crawl = False
                break
        if line.strip() == '---':
            if not crawl:
                crawl = True
            else:
                crawl = False
                break
    f.close()
total_tags = set(total_tags)

old_tags = glob.glob(tag_dir + '*.md')
for tag in old_tags:
    os.remove(tag)
if not os.path.exists(tag_dir):
    os.makedirs(tag_dir)


for tag in total_tags:
    tag = tag.strip("[]")
    tag_filename = tag_dir + tag + '.md'
    f = open(tag_filename, 'a', encoding="utf8")
    write_str = '---\nlayout: tag_index\nregenerate: true\ntitle: \"Tag: ' + tag + '\"\ntag: ' + tag + '\n---\n'
    f.write(write_str)
    f.close()
print("Tags generated, count", total_tags.__len__())
