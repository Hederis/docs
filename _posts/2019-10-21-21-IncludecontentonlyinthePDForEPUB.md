---
layout: default
title:  "Include content only in the PDF or EPUB"
permalink:  /include-custom-content/
categories: [Manuscripts and Book Text]
tags: [convert,typeset]
published: true
---

<section data-type="chapter" class="hsecchapter" data-hederis-type="hsecchapter" id="include-custom-content" data-pi-attrs="id: include-custom-content; data-tags: convert,typeset;" role="doc-chapter" data-tags="convert,typeset" data-author-name=" " data-book-title=" " title="Include content only in the PDF or EPUB"><h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="p5rggu7n6">Include content only in the PDF or EPUB</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="pBtNOdA2V">You can designate part of the content in your to appear only in the PDF or EPUB output by using a processing instruction (see &#8220;<a href="{% post_url 2019-10-21-35-Addspeciallayoutinstructions %}" id="p4tPgiCSH"><span class="Hyperlink" id="pzsF4VLKO">Add special layout instructions</span></a>&#8221;). The example below displays a different ISBN on the copyright page, depending on whether the output format is PDF or EPUB.</p>
    <img data-hederis-type="hblkimg" class="hblkimg" id="pQ4Zx1qZb" src="/images/customcontent1.png" data-img-src="customcontent1.png"/>
    <ol class="hwprnumlist" data-hederis-type="hwprnumlist" id="pg1Zeo5rz"><li class="hblkoli" data-hederis-type="hblkoli" id="li60BH5RKU"><p class="hblkoli" data-hederis-type="hblklip" id="pGkeMjawi">In your Word manuscript, find the paragraph, section, or wrapper that you want to hide in certain output formats.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="li0geN2A2U"><p class="hblkoli" data-hederis-type="hblklip" id="psty5qlvr">If it&#8217;s a paragraph, insert a new paragraph below it. If it&#8217;s a section, insert a new paragraph just below the section break paragraph (see &#8220;<a href="{% post_url 2019-10-21-18-AddaSection %}" id="ppYslxIlu"><span class="Hyperlink" id="p940Ye5Ac">Add a Section</span></a>&#8221;). If it&#8217;s a wrapper, insert a new paragraph after either the start or end of the wrapper (see &#8220;<a href="{% post_url 2019-10-21-17-AddaWrapper %}" id="pFxIro0SA"><span class="Hyperlink" id="pik9oS2Lh">Add a Wrapper</span></a>&#8221;). Here&#8217;s an example of a processing instruction applied to a whole section:</p><img data-hederis-type="hblkimg" class="hblkimg" id="pCxlnpVuS" src="/images/customcontent2.png" data-img-src="customcontent2.png"/>
    </li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="liYLCFy5v0"><p class="hblkoli" data-hederis-type="hblklip" id="pZFjuyW7w">Style your new paragraph with the &#8220;HED Processing instruction&#8221; style (see Fine-tune Word Styles&#8221;).</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="liUYlxKSU7"><p class="hblkoli" data-hederis-type="hblklip" id="ptqBhkhIv">Type the following text inside your new HED Processing instruction paragraph: FORMAT=, and then type one of the following keywords, depending on which output format you want the element to appear in: ebook, print.</p></li>
    </ol>
    </section>
    