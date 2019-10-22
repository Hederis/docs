---
layout: default
title:  "Custom Code Library"
permalink:  /custom-style-library/
categories: [Appendix]
tags: [convert]
published: true
---

<section data-type="appendix" class="hsecappendix" data-hederis-type="hsecappendix" id="custom-style-library" data-pi-attrs="id: custom-style-library; data-tags: convert;" role="doc-appendix" data-tags="convert" data-author-name=" " data-book-title=" " title="Custom Code Library"><h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="pMVubp58t">Custom Code Library</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="pOZngvElJ">Here are some custom processing instructions that you can copy, for frequently-requested customizations:</p>
    <section class="hwprsubsection" data-hederis-type="hwprsubsection" id="p9nKZCRUF" data-type="subsection" title="Override the author name in the running header"><h1 data-hederis-type="hblktitle" class="hblktitle" id="psH5A88gY">Override the author name in the running header</h1>
    <div class="hwprliteral" data-hederis-type="hwprliteral" id="ppAZdxR66" data-type="programlisting" role="doc-example"><p class="hblkcode" data-hederis-type="hblkcode" id="pN4WDPCFC">GLOBAL STYLE= string-set: authorname attr(data-author-name); SCOPE-BODY+ATTRS=data-author-name: <strong class="hspanstrong" data-hederis-type="hspanstrong" id="pXHomgcRZ">INSERT YOUR NAME</strong> SCOPE-BODY;</p></div>
    <p class="hblkp" data-hederis-type="hblkp" id="pDFj4e3qE">This processing instruction allows you to override the author name that appears in the running header of your predefined template; include it after any paragraph, wrapper, or section. The author name text is traditionally pulled from any paragraph on your title page that is tagged with the <span class="Emphasis" id="pkyqh22Yd"><em class="hspanem" data-hederis-type="hspanem" id="pME2hWprF">HED Author name</em></span> style; by using this processing instruction, you override that default text.</p>
    <p class="hblkp" data-hederis-type="hblkp" id="pG74sRwVM">This processing instruction consists of two parts: a GLOBAL STYLE instruction that applies your custom text to the entire manuscript, and then an ATTRS instruction that contains a custom attribute with your new author name text, which will be applied to the main body container of your manuscript. In this snippet, the only bit that you need to change is the bolded &#8220;INSERT YOUR NAME&#8221; text &#8211; replace this with the text of your choice.</p>
    </section>
    <section class="hwprsubsection" data-hederis-type="hwprsubsection" id="p2MnzIARQ" data-type="subsection" title="Override the book title in the running header"><h1 data-hederis-type="hblktitle" class="hblktitle" id="p9G5tfeRy">Override the book title in the running header</h1>
    <div class="hwprliteral" data-hederis-type="hwprliteral" id="pcJWc9Ro2" data-type="programlisting" role="doc-example"><p class="hblkcode" data-hederis-type="hblkcode" id="pg2drUwvz">GLOBAL STYLE= string-set: booktitle attr(data-book-title); SCOPE-BODY+ATTRS=data-book-title: <strong class="hspanstrong" data-hederis-type="hspanstrong" id="pRlDiRk5A">INSERT YOUR TITLE</strong> SCOPE-BODY;</p></div>
    <p class="hblkp" data-hederis-type="hblkp" id="p2RcVcoWN">This processing instruction allows you to override the book title that appears in the running header of your predefined template; include it after any paragraph, wrapper, or section. The book title text is traditionally pulled from any paragraph on your title page that is tagged with the <span class="Emphasis" id="p30NH6GB5"><em class="hspanem" data-hederis-type="hspanem" id="p0BwqjCOH">HED Chapter title</em></span> style; by using this processing instruction, you override that default text.</p>
    <p class="hblkp" data-hederis-type="hblkp" id="p1JIJUJyN">This processing instruction consists of two parts: a GLOBAL STYLE instruction that applies your custom text to the entire manuscript, and then an ATTRS instruction that contains a custom attribute with your new book title text, which will be applied to the main body container of your manuscript. In this snippet, the only bit that you need to change is the bolded &#8220;INSERT YOUR TITLE&#8221; text &#8211; replace this with the text of your choice.</p>
    </section>
    </section>
    