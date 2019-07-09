# Process

Make changes to the Word file in this repo. Make sure that you give every new section you add a custom ID attribute (read the docs to learn how to do this) - this id will be used as the permalink for that section.

Run through the ingestion toolchain and extract sections.

Run the preparesite.py script that is in this repo, providing the required paths and filenames, e.g.: 

```
python3 /Users/nellie/git/hederis/docs/preparesite.py -i /Users/nellie/Documents/hederis/docs/conversion/ -o /Users/nellie/Documents/hederis/docs/gen/ -f /Users/nellie/Documents/hederis/docs/conversion/8539KFwUe6aQN3zivDHw.html
```

Add this to the top of the Convert:Quick Start file:

```html
&lt;iframe width="560" height="315" src="https://www.youtube.com/embed/vyuVLK4JIkg" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen>&lt;/iframe>
```

Copy all files *except* for the titlepage into the posts folder.

jekyll build, then commit and push.