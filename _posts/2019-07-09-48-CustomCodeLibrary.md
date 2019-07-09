---
layout: default
title:  "Custom Code Library"
permalink:  /custom-style-library/
categories: [Appendix]
tags: [convert]
published: true
---

<section data-type="appendix" class="hsecappendix" data-hederis-type="hsecappendix" id="custom-style-library" data-pi-attrs="id: custom-style-library; data-tags: convert;" role="doc-appendix" data-tags="convert" data-author-name=" " data-book-title=" " title="Custom Code Library"><h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="phYcC0lIn">Custom Code Library</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="p0vJ49597">Here are some custom processing instructions that you can copy, for frequently-requested customizations:</p>
    <section class="hwprsubsection" data-hederis-type="hwprsubsection" id="p2ErAudz9" data-type="subsection" title="Override the author name in the running header"><h1 data-hederis-type="hblktitle" class="hblktitle" id="pMvofuWgn">Override the author name in the running header</h1>
    <div class="hwprliteral" data-hederis-type="hwprliteral" id="pLCA8dcdj" data-type="programlisting" role="doc-example"><p class="hblkcode" data-hederis-type="hblkcode" id="pOWQ8zz4Y">GLOBAL STYLE= string-set: authorname attr(data-author-name); SCOPE-BODY+ATTRS=data-author-name: <strong data-hederis-type="hspanstrong">INSERT YOUR NAME</strong> SCOPE-BODY;</p></div>
    <p class="hblkp" data-hederis-type="hblkp" id="p9X9rrcfL">This processing instruction allows you to override the author name that appears in the running header of your predefined template; include it after any paragraph, wrapper, or section. The author name text is traditionally pulled from any paragraph on your title page that is tagged with the <em data-hederis-type="hspanem">HED Author name</em> style; by using this processing instruction, you override that default text.</p>
    <p class="hblkp" data-hederis-type="hblkp" id="pSREvZPjm">This processing instruction consists of two parts: a GLOBAL STYLE instruction that applies your custom text to the entire manuscript, and then an ATTRS instruction that contains a custom attribute with your new author name text, which will be applied to the main body container of your manuscript. In this snippet, the only bit that you need to change is the bolded &#8220;INSERT YOUR NAME&#8221; text &#8211; replace this with the text of your choice.</p>
    </section>
    <section class="hwprsubsection" data-hederis-type="hwprsubsection" id="pVWiGZCak" data-type="subsection" title="Override the book title in the running header"><h1 data-hederis-type="hblktitle" class="hblktitle" id="pVycXGaot">Override the book title in the running header</h1>
    <div class="hwprliteral" data-hederis-type="hwprliteral" id="pdxot0VYi" data-type="programlisting" role="doc-example"><p class="hblkcode" data-hederis-type="hblkcode" id="p4idNsphd">GLOBAL STYLE= string-set: booktitle attr(data-book-title); SCOPE-BODY+ATTRS=data-book-title: <strong data-hederis-type="hspanstrong">INSERT YOUR </strong><strong data-hederis-type="hspanstrong">TITLE</strong> SCOPE-BODY;</p></div>
    <p class="hblkp" data-hederis-type="hblkp" id="phmBaPNNr">This processing instruction allows you to override the book title that appears in the running header of your predefined template; include it after any paragraph, wrapper, or section. The book title text is traditionally pulled from any paragraph on your title page that is tagged with the <em data-hederis-type="hspanem">HED </em><em data-hederis-type="hspanem">Chapter</em><em data-hederis-type="hspanem"> </em><em data-hederis-type="hspanem">title</em> style; by using this processing instruction, you override that default text.</p>
    <p class="hblkp" data-hederis-type="hblkp" id="px2tEq6OH">This processing instruction consists of two parts: a GLOBAL STYLE instruction that applies your custom text to the entire manuscript, and then an ATTRS instruction that contains a custom attribute with your new book title text, which will be applied to the main body container of your manuscript. In this snippet, the only bit that you need to change is the bolded &#8220;INSERT YOUR TITLE&#8221; text &#8211; replace this with the text of your choice.</p>
    </section>
    </section>
    