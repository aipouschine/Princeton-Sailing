#!/bin/bash

echo "Rendering Markdown..."
perl Markdown.pl text/home_text.text > text/home_text.html
echo "Done."
echo "Rendering templates..."
python render_templates.py
echo "Done."
echo "Rendering and compressing css files..."
lessc --yui-compress site/static/base.less site/static/base.css
echo "Done."
# echo "Uploading to server..."
#! rsync -ahvP --delete /Users/default/fun/sailing agrasso@arizona.princeton.edu:/u/agrasso/public_html/sailing
# echo "Done"
