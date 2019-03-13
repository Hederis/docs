---
layout: default
title:  "Include content only in the PDF or EPUB"
categories: [Manuscripts and Book Text]
published: true
---

<section data-type="chapter" class="hsecchapter" data-hederis-type="hsecchapter" id="pT1by0uwK"><h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="pADSEXOjc">Include content only in the PDF or EPUB</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="pqPqPDyGt">You can designate part of the content in your to appear only in the PDF or EPUB output by using a processing instruction (see &#8220;<a href="{% post_url 2019-03-12-22-Addspecialdesigninstructions %}" id="pUBq4VyWb"><span class="Hyperlink" id="pHlegFAsY">Add special design instructions</span></a>&#8221;). The example below displays a different ISBN on the copyright page, depending on whether the output format is PDF or EPUB.</p>
    <img data-hederis-type="hblkimg" class="hblkimg" id="p6QTTqNAI" src="/images/customcontent1.png"/>
    <ol class="hwprnum-liststart" data-hederis-type="hwprnum-liststart" id="pazbp1rwy"><li class="hblkoli" data-hederis-type="hblkoli" id="liC4A5imL1"><p class="hblkoli" data-hederis-type="hblkoli" id="pQxThEa1S">In your Word manuscript, find the paragraph, section, or wrapper that you want to hide in certain output formats.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="liGGP95fLn"><p class="hblkoli" data-hederis-type="hblkoli" id="p3eFUUr8h">If it&#8217;s a paragraph, insert a new paragraph below it. If it&#8217;s a section, insert a new paragraph just below the section break paragraph (see &#8220;<a href="{% post_url 2019-03-12-15-AddaSection %}" id="pngFdertx"><span class="Hyperlink" id="p4R9rnWJl">Add a Section</span></a>&#8221;). If it&#8217;s a wrapper, insert a new paragraph after either the start or end of the wrapper (see &#8220;<a href="{% post_url 2019-03-12-14-AddaWrapper %}" id="pFJL3bJFh"><span class="Hyperlink" id="pEthbRRMh">Add a Wrapper</span></a>&#8221;). Here&#8217;s an example of a processing instruction applied to a whole section:</p><img data-hederis-type="hblkimg" class="hblkimg" id="pkxZexODr" src="/images/customcontent2.png"/>
    </li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="li3EhdvEiJ"><p class="hblkoli" data-hederis-type="hblkoli" id="pLYe2g8qm">Style your new paragraph with the &#8220;HED Processing instruction&#8221; style (see Fine-tune Word Styles&#8221;).</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="liVHPvFSX9"><p class="hblkoli" data-hederis-type="hblkoli" id="pTtPa5kca">Type the following text inside your new HED Processing instruction paragraph: FORMAT=, and then type one of the following keywords, depending on which output format you want the element to appear in: ebook, print.</p></li>
    </ol>
    </section>
    