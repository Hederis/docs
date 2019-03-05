---
layout: default
title:  "Include content only in the PDF or EPUB"
categories: [Manuscripts and Book Text]
published: true
---

<section data-type="chapter" class="hsecchapter" data-hederis-type="hsecchapter" id="psAkctrfl"><h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="pTqgz0EkG">Include content only in the PDF or EPUB</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="pZdB3yvyY">You can designate part of the content in your to appear only in the PDF or EPUB output by using a processing instruction (see &#8220;<a href="{% post_url 2019-03-04-22-Addspecialdesigninstructions %}" id="p1pG3hlPR"><span class="Hyperlink" id="pRGLS6qNP">Add special design instructions</span></a>&#8221;). The example below displays a different ISBN on the copyright page, depending on whether the output format is PDF or EPUB.</p>
    <img data-hederis-type="hblkimg" class="hblkimg" id="pwL02qn6N" src="/images/customcontent1.png"/>
    <ol class="hwprnum-liststart" data-hederis-type="hwprnum-liststart" id="pA6vKixpO"><li class="hblkoli" data-hederis-type="hblkoli" id="liKSM9pVzz"><p class="hblkoli" data-hederis-type="hblkoli" id="pxsBXO1Xx">In your Word manuscript, find the paragraph, section, or wrapper that you want to hide in certain output formats.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="likKzX7G5g"><p class="hblkoli" data-hederis-type="hblkoli" id="pVV0j0s4H">If it&#8217;s a paragraph, insert a new paragraph below it. If it&#8217;s a section, insert a new paragraph just below the section break paragraph (see &#8220;<a href="{% post_url 2019-03-04-15-AddaSection %}" id="piMSmRbmE"><span class="Hyperlink" id="poHOLR2iH">Add a Section</span></a>&#8221;). If it&#8217;s a wrapper, insert a new paragraph after either the start or end of the wrapper (see &#8220;<a href="{% post_url 2019-03-04-14-AddaWrapper %}" id="pZrjPMQVm"><span class="Hyperlink" id="pQRuLNZV2">Add a Wrapper</span></a>&#8221;). Here&#8217;s an example of a processing instruction applied to a whole section:</p><img data-hederis-type="hblkimg" class="hblkimg" id="pF1JHR9bU" src="/images/customcontent2.png"/>
    </li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="livsmzFbK3"><p class="hblkoli" data-hederis-type="hblkoli" id="p11YJ3bWR">Style your new paragraph with the &#8220;HED Processing instruction&#8221; style (see Fine-tune Word Styles&#8221;).</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="liZM2tePyk"><p class="hblkoli" data-hederis-type="hblkoli" id="pLGNgwOTn">Type the following text inside your new HED Processing instruction paragraph: FORMAT=, and then type one of the following keywords, depending on which output format you want the element to appear in: ebook, print.</p></li>
    </ol>
    </section>
    