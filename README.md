Princeton-Sailing
=================

Princeton Sailing website redesign

Dependencies: python, lessc, Python-Markdown

Upkeep
======
### How to change the roster

The roster information is stored in data/roster.json. You can pretty much get a sense of what an entry should look like by poking around in there. The one thing that might get you is that all entries (except the last!) need to be followed by a comma. Add roster photos to the directory site/static/img, with the title [netid].jpg. They'll get put in automatically from there. Try to use photos with a bit of a portrait orientation if possible - it makes them behave a little better.

### How to change the schedule

The schedule is stored in data/schedule.json. As with the roster, you can prety much figure out how this should go by looking at it.

### How to change text on a page

The texts for the Home page, Alumni page, News page, and Contact page live in text/home_text.text, text/alumni_text.text, text/news_text.text, and text/contact_text.text, respectively. NOTE: do not modify text/[anything].html. These are generated files.

To get that beautiful styling we want, articles should be wrapped in

    <div class="article" markdown="1">
    Your article here...
    </div>

Basically, we want to be able to send a little HTML formatting through the preprocessor in a way that standard Markdown doesn't let us. This lets us do that.

### Build and preview your changes

To build the site, run ./update_site.sh. 

To preview your changes and make sure that their sane, point your browser to file:///[path to this directory]/site/index.html

Once everythign looks ok, you can go ahead and deploy your changes.

### Deploy your changes to the site

Remember to build and preview before you deploy! If you don't build the site, nothing will actually change.

The simplest way to deploy is to run ./deploy.sh, which is just a wrapper around rsync, a really handy tool for updating changes to a directory.

### Push your changes to Github

If you've modified any of the source files, please remember to commit and push to Github. It's cleanest if we keep the source data here.
