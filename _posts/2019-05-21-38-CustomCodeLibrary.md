---
layout: default
title:  "Custom Code Library"
permalink:  /custom-style-library/
categories: [Appendix]
published: true
---

<section data-type="appendix" class="hsecappendix" data-hederis-type="hsecappendix" id="custom-style-library" data-pi-attrs="id: custom-style-library" role="doc-appendix" title="Custom Code Library"><h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="p5JUQEm8n">Custom Code Library</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="pQYSJayf7">Here are some custom processing instructions that you can copy, for frequently-requested customizations:</p>
    <section class="hwprsubsection" data-hederis-type="hwprsubsection" id="p9qov4Fpd" data-type="subsection" title="Override the author name in the running header"><h1 data-hederis-type="hblktitle" class="hblktitle" id="prCSNo9jf">Override the author name in the running header</h1>
    <div class="hwprliteral" data-hederis-type="hwprliteral" id="pK6nsfnPO" data-type="programlisting" role="doc-example"><p class="hblkcode" data-hederis-type="hblkcode" id="pkFd2pSLz">GLOBAL STYLE= string-set: authorname attr(data-author-name); SCOPE-BODY+ATTRS=data-author-name: <strong>INSERT YOUR NAME</strong> SCOPE-BODY;</p></div>
    <p class="hblkp" data-hederis-type="hblkp" id="pUdEZ440O">This processing instruction allows you to override the author name that appears in the running header of your predefined template; include it after any paragraph, wrapper, or section. The author name text is traditionally pulled from any paragraph on your title page that is tagged with the <em>HED Author name</em> style; by using this processing instruction, you override that default text.</p>
    <p class="hblkp" data-hederis-type="hblkp" id="pTTYhvN5Q">This processing instruction consists of two parts: a GLOBAL STYLE instruction that applies your custom text to the entire manuscript, and then an ATTRS instruction that contains a custom attribute with your new author name text, which will be applied to the main body container of your manuscript. In this snippet, the only bit that you need to change is the bolded &#8220;INSERT YOUR NAME&#8221; text &#8211; replace this with the text of your choice.</p>
    </section>
    <section class="hwprsubsection" data-hederis-type="hwprsubsection" id="pJnFhYTA6" data-type="subsection" title="Override the book title in the running header"><h1 data-hederis-type="hblktitle" class="hblktitle" id="peBGEyWAl">Override the book title in the running header</h1>
    <div class="hwprliteral" data-hederis-type="hwprliteral" id="p6Qo6l1QZ" data-type="programlisting" role="doc-example"><p class="hblkcode" data-hederis-type="hblkcode" id="pvjZ3qoZJ">GLOBAL STYLE= string-set: booktitle attr(data-book-title); SCOPE-BODY+ATTRS=data-book-title: <strong>INSERT YOUR </strong><strong>TITLE</strong> SCOPE-BODY;</p></div>
    <p class="hblkp" data-hederis-type="hblkp" id="p9szWLu5w">This processing instruction allows you to override the book title that appears in the running header of your predefined template; include it after any paragraph, wrapper, or section. The book title text is traditionally pulled from any paragraph on your title page that is tagged with the <em>HED </em><em>Chapter</em><em> </em><em>title</em> style; by using this processing instruction, you override that default text.</p>
    <p class="hblkp" data-hederis-type="hblkp" id="pdFVXYPLP">This processing instruction consists of two parts: a GLOBAL STYLE instruction that applies your custom text to the entire manuscript, and then an ATTRS instruction that contains a custom attribute with your new book title text, which will be applied to the main body container of your manuscript. In this snippet, the only bit that you need to change is the bolded &#8220;INSERT YOUR TITLE&#8221; text &#8211; replace this with the text of your choice.</p>
    </section>
    </section>
    