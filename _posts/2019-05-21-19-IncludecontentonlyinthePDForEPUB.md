---
layout: default
title:  "Include content only in the PDF or EPUB"
permalink:  /include-custom-content/
categories: [Manuscripts and Book Text]
published: true
---

<section data-type="chapter" class="hsecchapter" data-hederis-type="hsecchapter" id="include-custom-content" data-pi-attrs="id: include-custom-content" role="doc-chapter" title="Include content only in the PDF or EPUB"><h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="paPr64bxf">Include content only in the PDF or EPUB</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="pr1EffLFT">You can designate part of the content in your to appear only in the PDF or EPUB output by using a processing instruction (see &#8220;<a href="{% post_url 2019-05-21-24-Addspeciallayoutinstructions %}"><span class="Hyperlink">Add special layout instructions</span></a>&#8221;). The example below displays a different ISBN on the copyright page, depending on whether the output format is PDF or EPUB.</p>
    <img data-hederis-type="hblkimg" class="hblkimg" id="pnuxkWIwR" src="/images/customcontent1.png"/>
    <ol class="hwprnum-list" data-hederis-type="hwprnum-list" id="pyh5c2SiD"><li class="hblkoli" data-hederis-type="hblkoli" id="li65eOf8bh"><p class="hblkoli" data-hederis-type="hblkoli" id="puOVSvwJp">In your Word manuscript, find the paragraph, section, or wrapper that you want to hide in certain output formats.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="liQOGMkWSq"><p class="hblkoli" data-hederis-type="hblkoli" id="padcYej22">If it&#8217;s a paragraph, insert a new paragraph below it. If it&#8217;s a section, insert a new paragraph just below the section break paragraph (see &#8220;<a href="{% post_url 2019-05-21-16-AddaSection %}"><span class="Hyperlink">Add a Section</span></a>&#8221;). If it&#8217;s a wrapper, insert a new paragraph after either the start or end of the wrapper (see &#8220;<a href="{% post_url 2019-05-21-15-AddaWrapper %}"><span class="Hyperlink">Add a Wrapper</span></a>&#8221;). Here&#8217;s an example of a processing instruction applied to a whole section:</p><img data-hederis-type="hblkimg" class="hblkimg" id="phn33bQZP" src="/images/customcontent2.png"/>
    </li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="limGdymCP0"><p class="hblkoli" data-hederis-type="hblkoli" id="pUgT8O88m">Style your new paragraph with the &#8220;HED Processing instruction&#8221; style (see Fine-tune Word Styles&#8221;).</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="li40VSyq7Q"><p class="hblkoli" data-hederis-type="hblkoli" id="pCQYfiIEx">Type the following text inside your new HED Processing instruction paragraph: FORMAT=, and then type one of the following keywords, depending on which output format you want the element to appear in: ebook, print.</p></li>
    </ol>
    </section>
    