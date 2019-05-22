---
layout: default
title:  "Include full-page images in the PDF"
permalink:  /include-full-page-images/
categories: [Images]
published: true
---

<section data-type="chapter" class="hsecchapter" data-hederis-type="hsecchapter" id="include-full-page-images" data-pi-attrs="id: include-full-page-images" role="doc-chapter" title="Include full-page images in the PDF"><h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="plPd2MMWW">Include full-page images in the PDF</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="pc8fKGUVU">By default, all images in the PDF will be sized down to fit within your specified margin and page dimensions (see &#8220;<a href="{% post_url 2019-05-22-21-AdjustPDFtrimsizeandmargins %}"><span class="Hyperlink">Adjust PDF trim size and margins</span></a>&#8221;). However, you may designate an image to be &#8220;full bleed&#8221;, which means that it will take up the entire page and extend into the bleed area beyond the page, creating a graphic that is flush with the edge of the book in the final product. To do so, you&#8217;ll need to use a process instruction (see &#8220;<a href="{% post_url 2019-05-22-24-Addspeciallayoutinstructions %}"><span class="Hyperlink">Add special layout instructions</span></a>&#8221;).</p>
    <ol class="hwprnum-list" data-hederis-type="hwprnum-list" id="pnPKsgmAy"><li class="hblkoli" data-hederis-type="hblkoli" id="liUOA0zc0f"><p class="hblkoli" data-hederis-type="hblkoli" id="pOhPWtNTI">In your Word manuscript, find the &#8220;HED Image holder&#8221; paragraph that contains your image filename.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="liRZj9p2TY"><p class="hblkoli" data-hederis-type="hblkoli" id="pqngJIJrM">Insert a new paragraph below your image holder paragraph, and apply the &#8220;HED Processing instruction&#8221; style to it.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="lixRtlR8U0"><p class="hblkoli" data-hederis-type="hblkoli" id="pmOHRdZO8">Type the following text inside your new HED Processing instruction paragraph: IMAGE-SIZE=fullbleed</p></li>
    </ol>
    <p class="hblkp" data-hederis-type="hblkp" id="pG8NTi3dd">Your Word manuscript should look like this:</p>
    <img data-hederis-type="hblkimg" class="hblkimg" id="pQNVq2yt3" src="/images/fullbleed_1.png"/>
    </section>
    