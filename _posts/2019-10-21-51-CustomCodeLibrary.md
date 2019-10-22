---
layout: default
title:  "Custom Code Library"
permalink:  /custom-style-library/
categories: [Appendix]
tags: [convert]
published: true
---

<section data-type="appendix" class="hsecappendix" data-hederis-type="hsecappendix" id="custom-style-library" data-pi-attrs="id: custom-style-library; data-tags: convert;" role="doc-appendix" data-tags="convert" data-author-name=" " data-book-title=" " title="Custom Code Library"><h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="pXJp2tuk4">Custom Code Library</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="pZCJHxHV5">Here are some custom processing instructions that you can copy, for frequently-requested customizations:</p>
    <section class="hwprsubsection" data-hederis-type="hwprsubsection" id="ppKWJ5miX" data-type="subsection" title="Override the author name in the running header"><h1 data-hederis-type="hblktitle" class="hblktitle" id="p1DuHd870">Override the author name in the running header</h1>
    <div class="hwprliteral" data-hederis-type="hwprliteral" id="pe5Klcm1b" data-type="programlisting" role="doc-example"><p class="hblkcode" data-hederis-type="hblkcode" id="pJC8xhLBk">GLOBAL STYLE= string-set: authorname attr(data-author-name); SCOPE-BODY+ATTRS=data-author-name: <strong class="hspanstrong" data-hederis-type="hspanstrong" id="phcOJkdkP">INSERT YOUR NAME</strong> SCOPE-BODY;</p></div>
    <p class="hblkp" data-hederis-type="hblkp" id="pzsWd6pMW">This processing instruction allows you to override the author name that appears in the running header of your predefined template; include it after any paragraph, wrapper, or section. The author name text is traditionally pulled from any paragraph on your title page that is tagged with the <span class="Emphasis" id="pcfn3cmoA"><em class="hspanem" data-hederis-type="hspanem" id="p6pRUVdR5">HED Author name</em></span> style; by using this processing instruction, you override that default text.</p>
    <p class="hblkp" data-hederis-type="hblkp" id="pYlz9Oxuj">This processing instruction consists of two parts: a GLOBAL STYLE instruction that applies your custom text to the entire manuscript, and then an ATTRS instruction that contains a custom attribute with your new author name text, which will be applied to the main body container of your manuscript. In this snippet, the only bit that you need to change is the bolded &#8220;INSERT YOUR NAME&#8221; text &#8211; replace this with the text of your choice.</p>
    </section>
    <section class="hwprsubsection" data-hederis-type="hwprsubsection" id="pseiP6R5v" data-type="subsection" title="Override the book title in the running header"><h1 data-hederis-type="hblktitle" class="hblktitle" id="pwfoQWef8">Override the book title in the running header</h1>
    <div class="hwprliteral" data-hederis-type="hwprliteral" id="pGKsNd4p2" data-type="programlisting" role="doc-example"><p class="hblkcode" data-hederis-type="hblkcode" id="pPznXeMEt">GLOBAL STYLE= string-set: booktitle attr(data-book-title); SCOPE-BODY+ATTRS=data-book-title: <strong class="hspanstrong" data-hederis-type="hspanstrong" id="pzLxL3Xnv">INSERT YOUR TITLE</strong> SCOPE-BODY;</p></div>
    <p class="hblkp" data-hederis-type="hblkp" id="pz9zhJN70">This processing instruction allows you to override the book title that appears in the running header of your predefined template; include it after any paragraph, wrapper, or section. The book title text is traditionally pulled from any paragraph on your title page that is tagged with the <span class="Emphasis" id="pKvIOcof1"><em class="hspanem" data-hederis-type="hspanem" id="pZoyozo7r">HED Chapter title</em></span> style; by using this processing instruction, you override that default text.</p>
    <p class="hblkp" data-hederis-type="hblkp" id="pv1IH7rls">This processing instruction consists of two parts: a GLOBAL STYLE instruction that applies your custom text to the entire manuscript, and then an ATTRS instruction that contains a custom attribute with your new book title text, which will be applied to the main body container of your manuscript. In this snippet, the only bit that you need to change is the bolded &#8220;INSERT YOUR TITLE&#8221; text &#8211; replace this with the text of your choice.</p>
    </section>
    </section>
    