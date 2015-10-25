#!/bin/bash

echo "Rendering templates..."
python render_templates.py
echo "Done."
echo "Rendering and compressing css files..."
lessc less/base.less site/static/css/base.css
echo "Done."
