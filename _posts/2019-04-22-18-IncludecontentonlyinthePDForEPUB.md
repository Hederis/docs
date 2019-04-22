---
layout: default
title:  "Include content only in the PDF or EPUB"
permalink:  /include-custom-content/
categories: [Manuscripts and Book Text]
published: true
---

<section data-type="chapter" class="hsecchapter" data-hederis-type="hsecchapter" id="include-custom-content" data-pi-attrs="id: include-custom-content" role="doc-chapter"><h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="pEai7ajCw">Include content only in the PDF or EPUB</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="pNc78YnK7">You can designate part of the content in your to appear only in the PDF or EPUB output by using a processing instruction (see &#8220;<a href="{% post_url 2019-04-22-23-Addspeciallayoutinstructions %}"><span class="Hyperlink">Add special layout instructions</span></a>&#8221;). The example below displays a different ISBN on the copyright page, depending on whether the output format is PDF or EPUB.</p>
    <img data-hederis-type="hblkimg" class="hblkimg" id="pxOlxBbwI" src="/images/customcontent1.png"/>
    <ol class="hwprnum-list" data-hederis-type="hwprnum-list" id="p46OgyIq0"><li class="hblkoli" data-hederis-type="hblkoli" id="li81PbzNoN"><p class="hblkoli" data-hederis-type="hblkoli" id="pYWEoT3CE">In your Word manuscript, find the paragraph, section, or wrapper that you want to hide in certain output formats.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="lim4yYsG9S"><p class="hblkoli" data-hederis-type="hblkoli" id="pp3RPS9Wk">If it&#8217;s a paragraph, insert a new paragraph below it. If it&#8217;s a section, insert a new paragraph just below the section break paragraph (see &#8220;<a href="{% post_url 2019-04-22-16-AddaSection %}"><span class="Hyperlink">Add a Section</span></a>&#8221;). If it&#8217;s a wrapper, insert a new paragraph after either the start or end of the wrapper (see &#8220;<a href="{% post_url 2019-04-22-15-AddaWrapper %}"><span class="Hyperlink">Add a Wrapper</span></a>&#8221;). Here&#8217;s an example of a processing instruction applied to a whole section:</p><img data-hederis-type="hblkimg" class="hblkimg" id="pSqjloEGi" src="/images/customcontent2.png"/>
    </li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="liu2gJj2jD"><p class="hblkoli" data-hederis-type="hblkoli" id="pqZ8vDz5U">Style your new paragraph with the &#8220;HED Processing instruction&#8221; style (see Fine-tune Word Styles&#8221;).</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="liWzxNH83y"><p class="hblkoli" data-hederis-type="hblkoli" id="plssErEgE">Type the following text inside your new HED Processing instruction paragraph: FORMAT=, and then type one of the following keywords, depending on which output format you want the element to appear in: ebook, print.</p></li>
    </ol>
    </section>
    