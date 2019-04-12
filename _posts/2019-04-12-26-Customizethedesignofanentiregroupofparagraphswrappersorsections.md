---
layout: default
title:  "Customize the design of an entire group of paragraphs, wrappers, or sections"
permalink:  /global-paragraph-design/
categories: [Design]
published: true
---

<section data-type="chapter" class="hsecchapter" data-hederis-type="hsecchapter" id="global-paragraph-design" data-pi-attrs="id: global-paragraph-design" role="doc-chapter"><h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="pORLtqUgA">Customize the design of an entire group of paragraphs, wrappers, or sections</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="p6Se96OKZ">You can also use processing instructions to customize the design of an entire style. For example, you can customize the design of every paragraph in your book that uses the &#8220;HED Box type&#8221; style. Similarly, you can customize the design of wrappers and sections in your book (for example, every letter in the book, or every appendix section). Follow the instructions in the previous section, but instead of using the STYLE processing instruction keyword, use GLOBAL STYLE, like this:</p>
    <img data-hederis-type="hblkimg" class="hblkimg" id="p8FOQ6UBZ" src="/images/globalstyle.png"/>
    <section class="hwprsubsection" data-hederis-type="hwprsubsection" id="pQ4Laqetk" data-type="subsection"><h1 data-hederis-type="hblktitle" class="hblktitle" id="pJZ8fmCoD">Using the SCOPE-BODY Option</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="prTKVRBjr">You can also apply styles to your entire document, by using the SCOPE-BODY option in your GLOBAL STYLE processing instruction. This will expand the scope of your custom styles, so that they apply to the entire body of your manuscript, rather than being limited to just a group of elements. To do this:</p>
    <ol class="hwprnum-list" data-hederis-type="hwprnum-list" id="p4Guzf4wL"><li class="hblkoli" data-hederis-type="hblkoli" id="liLHf7eJ99"><p class="hblkoli" data-hederis-type="hblkoli" id="pYVyImzST">Type your GLOBAL STYLE processing instruction, as described above.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="lifoAKUoPD"><p class="hblkoli" data-hederis-type="hblkoli" id="pPjgOzfN6">At the very end of this processing instruction (but before any additional processing instructions that you&#8217;ll be adding via the &#8220;+&#8221; option, as described in &#8220;<a href="{% post_url 2019-04-12-23-Addspeciallayoutinstructions %}"><span class="Hyperlink">Add special layout instructions</span></a>&#8221;), type: SCOPE-BODY.</p></li>
    </ol>
    <p class="hblkp" data-hederis-type="hblkp" id="pKy7ZTjhX">Your styles will now be applied to the entire manuscript.</p>
    <figure class="hwprfig" data-hederis-type="hwprfig" id="pUtgYbLQa"><img data-hederis-type="hblkimg" class="hblkimg" id="pMxogHZDV" src="/images/globalscopebody.png"/>
    <p class="hblkcaption" data-hederis-type="hblkcaption" id="pagmnwp7p">In this processing instruction, we&#8217;re overriding the running header text with our own custom text. You can read more about this code snippet in &#8220;<a href="{% post_url 2019-04-12-32-CustomStyleLibrary %}"><span class="Hyperlink">Custom Styles Library</span></a>&#8221;.</p>
    </figure>
    </section>
    </section>
    