---
layout: default
title:  "Customize the design of an entire group of paragraphs, wrappers, or sections"
permalink:  /global-paragraph-design/
categories: [Design]
tags: [convert]
published: true
---

<section data-type="chapter" class="hsecchapter" data-hederis-type="hsecchapter" id="global-paragraph-design" data-pi-attrs="id: global-paragraph-design; data-tags: convert;" role="doc-chapter" data-tags="convert" data-author-name=" " data-book-title=" " title="Customize the design of an entire group of paragraphs, wrappers, or sections"><h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="pEQjQTfbq">Customize the design of an entire group of paragraphs, wrappers, or sections</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="pxdhczMav">You can also use processing instructions to customize the design of an entire style. For example, you can customize the design of every paragraph in your book that uses the &#8220;HED Box type&#8221; style. Similarly, you can customize the design of wrappers and sections in your book (for example, every letter in the book, or every appendix section). Follow the instructions in the previous section, but instead of using the STYLE processing instruction keyword, use GLOBAL STYLE, like this:</p>
    <img data-hederis-type="hblkimg" class="hblkimg" id="psNrRD0ZT" src="/images/globalstyle.png" data-img-src="globalstyle.png"/>
    <section class="hwprsubsection" data-hederis-type="hwprsubsection" id="pMLArVOuX" data-type="subsection" title="Using the SCOPE-BODY Option"><h1 data-hederis-type="hblktitle" class="hblktitle" id="p4l5lYrKV">Using the SCOPE-BODY Option</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="pPJ2InBU9">You can also apply styles to your entire document, by using the SCOPE-BODY option in your GLOBAL STYLE processing instruction. This will expand the scope of your custom styles, so that they apply to the entire body of your manuscript, rather than being limited to just a group of elements. To do this:</p>
    <ol class="hwprnumlist" data-hederis-type="hwprnumlist" id="pFOw64ICX"><li class="hblkoli" data-hederis-type="hblkoli" id="li0oqzOGWA"><p class="hblkoli" data-hederis-type="hblklip" id="pDwymJq1n">Type your GLOBAL STYLE processing instruction, as described above.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="liAsAhP3Ua"><p class="hblkoli" data-hederis-type="hblklip" id="pHF4I8BQQ">At the very end of this processing instruction (but before any additional processing instructions that you&#8217;ll be adding via the &#8220;+&#8221; option, as described in &#8220;<a href="{% post_url 2019-10-21-35-Addspeciallayoutinstructions %}" id="pX4VBqozu"><span class="Hyperlink" id="pS85raB1m">Add special layout instructions</span></a>&#8221;), type: SCOPE-BODY.</p></li>
    </ol>
    <p class="hblkp" data-hederis-type="hblkp" id="pwktpv2k3">Your styles will now be applied to the entire manuscript.</p>
    <figure class="hwprfig" data-hederis-type="hwprfig" id="pOh2EwerE"><img data-hederis-type="hblkimg" class="hblkimg" id="pW7VymPHT" src="/images/globalscopebody.png" data-img-src="globalscopebody.png"/>
    <p class="hblkcaption" data-hederis-type="hblkcaption" id="pnM69hDba">In this processing instruction, we&#8217;re overriding the running header text with our own custom text. You can read more about this code snippet in &#8220;<a href="{% post_url 2019-10-21-51-CustomCodeLibrary %}" id="pJvk41Ql0"><span class="Hyperlink" id="pmV1a3gI7">Custom Styles Library</span></a>&#8221;.</p>
    </figure>
    </section>
    </section>
    