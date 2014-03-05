#!/bin/bash

echo "Rendering templates..."
python render_templates.py
echo "Done."
echo "Rendering and compressing css files..."
lessc --yui-compress site/static/base.less site/static/base.css
echo "Done."
