# Hederis Documentation

## Contributing

* Create a Microsoft Word file for your new article.
* Give it a meaningful, searchable name. Think about the terms a user might search for related to your article topic, and try to include those in the article title.
* Make sure the Word file is tagged using Hederis Word styles.
* If you need to link to other sections of the documentation, create the link in Microsoft Word, and link to the required .docx file. This link will automatically be converted to a link to the final post, and the link text will be replaced with the linked .docx title.

## Generating

### To Convert a Single File:

* Save the file in the _word folder.
* Make sure to add the new article under the appropriate section heading in the Docs TOC, in data/navigation_docs.yml
* Push your branch up to github, and submit a pull request.
* Convert any revised or new .docx files to HTML via the standard Hederis scripts.
* Save the new HTML file in the _html directory.
* Convert the HTML file to markdown using the included convert_to_markdown.rb script, like this:

```
ruby convert_to_markdown.rb _html/html_file.html
```

### To Convert All Files At Once:

* Run the convert_to_markdown script without any arguments, as follows. Note that it requires the presence of the convert_docs.py script in the main hederis repo.

```
ruby convert_to_markdown.rb
```

### Push to Repo

Once the files are converted, add all changed files to your commit:

```
git add -u
```

Then commit:

```
git commit -m'your message here'
```

And push!