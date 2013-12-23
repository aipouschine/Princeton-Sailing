TEMPLATES:=$(wildcard templates/*.html)
LESS:=$(wildcard site/static/*.less)

all: templates css

templates: $(TEMPLATES)
	python render_templates.py

css: $(LESS)
	lessc --yui-compress site/static/base.less site/static/base.css
