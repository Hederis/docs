---
layout: default
title:  "Customize the design of an entire group of paragraphs, wrappers, or sections"
permalink:  /global-paragraph-design/
categories: [Design]
tags: [convert]
published: true
---

<section data-type="chapter" class="hsecchapter" data-hederis-type="hsecchapter" id="global-paragraph-design" data-pi-attrs="id: global-paragraph-design; data-tags: convert;" role="doc-chapter" data-tags="convert" data-author-name=" " data-book-title=" " title="Customize the design of an entire group of paragraphs, wrappers, or sections"><h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="p7kLRgE8v">Customize the design of an entire group of paragraphs, wrappers, or sections</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="pb7FXNr8B">You can also use processing instructions to customize the design of an entire style. For example, you can customize the design of every paragraph in your book that uses the &#8220;HED Box type&#8221; style. Similarly, you can customize the design of wrappers and sections in your book (for example, every letter in the book, or every appendix section). Follow the instructions in the previous section, but instead of using the STYLE processing instruction keyword, use GLOBAL STYLE, like this:</p>
    <img data-hederis-type="hblkimg" class="hblkimg" id="pnstwwBJO" src="/images/globalstyle.png"/>
    <section class="hwprsubsection" data-hederis-type="hwprsubsection" id="piDamrSaf" data-type="subsection" title="Using the SCOPE-BODY Option"><h1 data-hederis-type="hblktitle" class="hblktitle" id="pDgrIGa0Y">Using the SCOPE-BODY Option</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="p14DlVZ7S">You can also apply styles to your entire document, by using the SCOPE-BODY option in your GLOBAL STYLE processing instruction. This will expand the scope of your custom styles, so that they apply to the entire body of your manuscript, rather than being limited to just a group of elements. To do this:</p>
    <ol class="hwprnum-list" data-hederis-type="hwprnum-list" id="pooTsIC4Z"><li class="hblkoli" data-hederis-type="hblkoli" id="liWL8v2BfC"><p class="hblkoli" data-hederis-type="hblkoli" id="pkIt6e5ff">Type your GLOBAL STYLE processing instruction, as described above.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="liVikYRozd"><p class="hblkoli" data-hederis-type="hblkoli" id="pcW8EAN86">At the very end of this processing instruction (but before any additional processing instructions that you&#8217;ll be adding via the &#8220;+&#8221; option, as described in &#8220;<a href="{% post_url 2019-07-09-32-Addspeciallayoutinstructions %}"><span class="Hyperlink">Add special layout instructions</span></a>&#8221;), type: SCOPE-BODY.</p></li>
    </ol>
    <p class="hblkp" data-hederis-type="hblkp" id="paI2d0ama">Your styles will now be applied to the entire manuscript.</p>
    <figure class="hwprfig" data-hederis-type="hwprfig" id="pU5RtK0uE"><img data-hederis-type="hblkimg" class="hblkimg" id="pyJmdmrYt" src="/images/globalscopebody.png"/>
    <p class="hblkcaption" data-hederis-type="hblkcaption" id="pHoPd5eZo">In this processing instruction, we&#8217;re overriding the running header text with our own custom text. You can read more about this code snippet in &#8220;<a href="{% post_url 2019-07-09-48-CustomCodeLibrary %}"><span class="Hyperlink">Custom Styles Library</span></a>&#8221;.</p>
    </figure>
    </section>
    </section>
    