---
layout: default
title:  "Custom Code Library"
permalink:  /custom-style-library/
categories: [Appendix]
published: true
---

<section data-type="appendix" class="hsecappendix" data-hederis-type="hsecappendix" id="custom-style-library" data-pi-attrs="id: custom-style-library" role="doc-appendix" title="Custom Code Library"><h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="poU7qd3Wv">Custom Code Library</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="pJKoQCoG8">Here are some custom processing instructions that you can copy, for frequently-requested customizations:</p>
    <section class="hwprsubsection" data-hederis-type="hwprsubsection" id="p2LgIM1GE" data-type="subsection" title="Override the author name in the running header"><h1 data-hederis-type="hblktitle" class="hblktitle" id="pL8OrqeOv">Override the author name in the running header</h1>
    <div class="hwprliteral" data-hederis-type="hwprliteral" id="pAxWhJ97q" data-type="programlisting" role="doc-example"><p class="hblkcode" data-hederis-type="hblkcode" id="pSxnzQ8Pr">GLOBAL STYLE= string-set: authorname attr(data-author-name); SCOPE-BODY+ATTRS=data-author-name: <strong>INSERT YOUR NAME</strong> SCOPE-BODY;</p></div>
    <p class="hblkp" data-hederis-type="hblkp" id="pTJuD2eq8">This processing instruction allows you to override the author name that appears in the running header of your predefined template; include it after any paragraph, wrapper, or section. The author name text is traditionally pulled from any paragraph on your title page that is tagged with the <em>HED Author name</em> style; by using this processing instruction, you override that default text.</p>
    <p class="hblkp" data-hederis-type="hblkp" id="piUpdjQ9y">This processing instruction consists of two parts: a GLOBAL STYLE instruction that applies your custom text to the entire manuscript, and then an ATTRS instruction that contains a custom attribute with your new author name text, which will be applied to the main body container of your manuscript. In this snippet, the only bit that you need to change is the bolded &#8220;INSERT YOUR NAME&#8221; text &#8211; replace this with the text of your choice.</p>
    </section>
    <section class="hwprsubsection" data-hederis-type="hwprsubsection" id="pQD0Y6dsI" data-type="subsection" title="Override the book title in the running header"><h1 data-hederis-type="hblktitle" class="hblktitle" id="pqVDx2uwv">Override the book title in the running header</h1>
    <div class="hwprliteral" data-hederis-type="hwprliteral" id="p3VN84BWX" data-type="programlisting" role="doc-example"><p class="hblkcode" data-hederis-type="hblkcode" id="p7RlG2VGS">GLOBAL STYLE= string-set: booktitle attr(data-book-title); SCOPE-BODY+ATTRS=data-book-title: <strong>INSERT YOUR </strong><strong>TITLE</strong> SCOPE-BODY;</p></div>
    <p class="hblkp" data-hederis-type="hblkp" id="pMgZXHLxt">This processing instruction allows you to override the book title that appears in the running header of your predefined template; include it after any paragraph, wrapper, or section. The book title text is traditionally pulled from any paragraph on your title page that is tagged with the <em>HED </em><em>Chapter</em><em> </em><em>title</em> style; by using this processing instruction, you override that default text.</p>
    <p class="hblkp" data-hederis-type="hblkp" id="pCRpqcnre">This processing instruction consists of two parts: a GLOBAL STYLE instruction that applies your custom text to the entire manuscript, and then an ATTRS instruction that contains a custom attribute with your new book title text, which will be applied to the main body container of your manuscript. In this snippet, the only bit that you need to change is the bolded &#8220;INSERT YOUR TITLE&#8221; text &#8211; replace this with the text of your choice.</p>
    </section>
    </section>
    