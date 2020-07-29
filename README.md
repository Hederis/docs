# Process

Make changes to the Word file in this repo. Make sure that you give every new section you add a custom ID attribute (read the docs to learn how to do this) - this id will be used as the permalink for that section.

Run through the ingestion toolchain and extract sections. You'll need to uncomment line 3761 in docx_convert.py (the line that starts with "sectionfiles, compiled = ").

Run the preparesite.py script that is in this repo, providing the required paths and filenames, e.g.: 

```
python3 /Users/nellie/git/hederis/docs/preparesite.py -i /Users/nellie/hederis/docs/conversion/ -o /Users/nellie/hederis/docs/gen/ -f /Users/nellie/hederis/docs/conversion/VSgABkJ2sBgf2aPB4ABY.html
```

Copy all files *except* for the titlepage ([DATE]_HederisDocumentation.md) into the posts folder.

Copy the `section` content from the titlepage into the site index.html file.

Build the site:

```
jekyll build
```

Then add all changed files (git add -A), commit, and push.