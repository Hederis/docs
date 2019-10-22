---
layout: default
title:  "Include content only in the PDF or EPUB"
permalink:  /include-custom-content/
categories: [Manuscripts and Book Text]
tags: [convert,typeset]
published: true
---

<section data-type="chapter" class="hsecchapter" data-hederis-type="hsecchapter" id="include-custom-content" data-pi-attrs="id: include-custom-content; data-tags: convert,typeset;" role="doc-chapter" data-tags="convert,typeset" data-author-name=" " data-book-title=" " title="Include content only in the PDF or EPUB"><h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="poKAUeT4w">Include content only in the PDF or EPUB</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="p9KirHFjW">You can designate part of the content in your to appear only in the PDF or EPUB output by using a processing instruction (see &#8220;<a href="{% post_url 2019-10-22-36-Addspeciallayoutinstructions %}" id="pFI53kjiB"><span class="Hyperlink" id="p6emkWfSE">Add special layout instructions</span></a>&#8221;). The example below displays a different ISBN on the copyright page, depending on whether the output format is PDF or EPUB.</p>
    <img data-hederis-type="hblkimg" class="hblkimg" id="pFkFzneX8" src="/images/customcontent1.png" data-img-src="customcontent1.png"/>
    <ol class="hwprnumlist" data-hederis-type="hwprnumlist" id="pB91rrYp3"><li class="hblkoli" data-hederis-type="hblkoli" id="liOo388wTt"><p class="hblkoli" data-hederis-type="hblklip" id="pSJSmMFw3">In your Word manuscript, find the paragraph, section, or wrapper that you want to hide in certain output formats.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="li3n5X0lnP"><p class="hblkoli" data-hederis-type="hblklip" id="pY5OP5bzr">If it&#8217;s a paragraph, insert a new paragraph below it. If it&#8217;s a section, insert a new paragraph just below the section break paragraph (see &#8220;<a href="{% post_url 2019-10-22-18-AddaSection %}" id="prpOcr0zl"><span class="Hyperlink" id="pE4Tm3dhY">Add a Section</span></a>&#8221;). If it&#8217;s a wrapper, insert a new paragraph after either the start or end of the wrapper (see &#8220;<a href="{% post_url 2019-10-22-17-AddaWrapper %}" id="pQE92tEKL"><span class="Hyperlink" id="pdd3O7cos">Add a Wrapper</span></a>&#8221;). Here&#8217;s an example of a processing instruction applied to a whole section:</p><img data-hederis-type="hblkimg" class="hblkimg" id="pPpSwWcoX" src="/images/customcontent2.png" data-img-src="customcontent2.png"/>
    </li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="liLepLQxiW"><p class="hblkoli" data-hederis-type="hblklip" id="pZK0lDZQQ">Style your new paragraph with the &#8220;HED Processing instruction&#8221; style (see Fine-tune Word Styles&#8221;).</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="liKjzIrGRg"><p class="hblkoli" data-hederis-type="hblklip" id="ptVS8dtum">Type the following text inside your new HED Processing instruction paragraph: FORMAT=, and then type one of the following keywords, depending on which output format you want the element to appear in: ebook, print.</p></li>
    </ol>
    </section>
    