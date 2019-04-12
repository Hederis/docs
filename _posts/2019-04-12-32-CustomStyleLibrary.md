---
layout: default
title:  "Custom Style Library"
permalink:  /custom-style-library/
categories: [Appendix]
published: true
---

<section data-type="appendix" class="hsecappendix" data-hederis-type="hsecappendix" id="custom-style-library" data-pi-attrs="id: custom-style-library" role="doc-appendix"><h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="p7UyKF62p">Custom Style Library</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="pLVfNDT9l">Here are some custom processing instructions that you can copy, for frequently-requested customizations:</p>
    <section class="hwprsubsection" data-hederis-type="hwprsubsection" id="p3WIWOG5k" data-type="subsection"><h1 data-hederis-type="hblktitle" class="hblktitle" id="pa361aqyU">Override the author name in the running header</h1>
    <div class="hwprliteral" data-hederis-type="hwprliteral" id="pMQ4TeR9g" data-type="programlisting" role="doc-example"><p class="hblkcode" data-hederis-type="hblkcode" id="pQN1LasH9">GLOBAL STYLE= string-set: authorname attr(data-author-name); SCOPE-BODY+ATTRS=data-author-name: <strong>INSERT YOUR NAME</strong> SCOPE-BODY;</p></div>
    <p class="hblkp" data-hederis-type="hblkp" id="pLXLA4O6r">This processing instruction allows you to override the author name that appears in the running header of your predefined template. The author name text is traditionally pulled from any paragraph on your title page that is tagged with the <em>HED Author name</em> style; by using this processing instruction, you override that default text.</p>
    <p class="hblkp" data-hederis-type="hblkp" id="p86bDhagx">This processing instruction consists of two parts: a GLOBAL STYLE instruction that applies your custom text to the entire manuscript, and then an ATTRS instruction that contains a custom attribute with your new author name text, which will be applied to the main body container of your manuscript. In this style snippet, the only bit that you need to change is the bolded &#8220;INSERT YOUR NAME&#8221; text &#8211; replace this with the text of your choice.</p>
    </section>
    </section>
    