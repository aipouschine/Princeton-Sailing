#!/bin/bash
this_dir=`dirname $0`

rsync -ahvP --delete $this_dir/site sailing@arizona.princeton.edu:/u/sailing/public_html
