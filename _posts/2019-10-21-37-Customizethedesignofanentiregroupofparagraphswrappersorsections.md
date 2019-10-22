---
layout: default
title:  "Customize the design of an entire group of paragraphs, wrappers, or sections"
permalink:  /global-paragraph-design/
categories: [Design]
tags: [convert]
published: true
---

<section data-type="chapter" class="hsecchapter" data-hederis-type="hsecchapter" id="global-paragraph-design" data-pi-attrs="id: global-paragraph-design; data-tags: convert;" role="doc-chapter" data-tags="convert" data-author-name=" " data-book-title=" " title="Customize the design of an entire group of paragraphs, wrappers, or sections"><h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="psmtHgBZT">Customize the design of an entire group of paragraphs, wrappers, or sections</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="pzJuaKHCu">You can also use processing instructions to customize the design of an entire style. For example, you can customize the design of every paragraph in your book that uses the &#8220;HED Box type&#8221; style. Similarly, you can customize the design of wrappers and sections in your book (for example, every letter in the book, or every appendix section). Follow the instructions in the previous section, but instead of using the STYLE processing instruction keyword, use GLOBAL STYLE, like this:</p>
    <img data-hederis-type="hblkimg" class="hblkimg" id="p3S3qZYLw" src="/images/globalstyle.png" data-img-src="globalstyle.png"/>
    <section class="hwprsubsection" data-hederis-type="hwprsubsection" id="pnAzKBYgM" data-type="subsection" title="Using the SCOPE-BODY Option"><h1 data-hederis-type="hblktitle" class="hblktitle" id="p5cMfDqMt">Using the SCOPE-BODY Option</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="p38we6vGH">You can also apply styles to your entire document, by using the SCOPE-BODY option in your GLOBAL STYLE processing instruction. This will expand the scope of your custom styles, so that they apply to the entire body of your manuscript, rather than being limited to just a group of elements. To do this:</p>
    <ol class="hwprnumlist" data-hederis-type="hwprnumlist" id="paA38L91C"><li class="hblkoli" data-hederis-type="hblkoli" id="livXtyIT6V"><p class="hblkoli" data-hederis-type="hblklip" id="pgEU2P66s">Type your GLOBAL STYLE processing instruction, as described above.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="lihf3spKrV"><p class="hblkoli" data-hederis-type="hblklip" id="p6tmREhGr">At the very end of this processing instruction (but before any additional processing instructions that you&#8217;ll be adding via the &#8220;+&#8221; option, as described in &#8220;<a href="{% post_url 2019-10-21-35-Addspeciallayoutinstructions %}" id="pWZyOFAkP"><span class="Hyperlink" id="pk3tZ24cO">Add special layout instructions</span></a>&#8221;), type: SCOPE-BODY.</p></li>
    </ol>
    <p class="hblkp" data-hederis-type="hblkp" id="pM9FHkD3v">Your styles will now be applied to the entire manuscript.</p>
    <figure class="hwprfig" data-hederis-type="hwprfig" id="pdOj13eoq"><img data-hederis-type="hblkimg" class="hblkimg" id="pF7sVcChU" src="/images/globalscopebody.png" data-img-src="globalscopebody.png"/>
    <p class="hblkcaption" data-hederis-type="hblkcaption" id="pAOJCybrf">In this processing instruction, we&#8217;re overriding the running header text with our own custom text. You can read more about this code snippet in &#8220;<a href="{% post_url 2019-10-21-51-CustomCodeLibrary %}" id="pbDGEL9C3"><span class="Hyperlink" id="pDjV3RQzP">Custom Styles Library</span></a>&#8221;.</p>
    </figure>
    </section>
    </section>
    