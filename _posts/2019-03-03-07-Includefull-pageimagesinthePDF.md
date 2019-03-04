---
layout: default
title:  "Include full-page images in the PDF"
categories: [Images]
published: true
---

<section data-type="chapter" class="hsecchapter" data-hederis-type="hsecchapter" id="pHlDGniRI"><h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="pynH4osPj">Include full-page images in the PDF</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="p6hLasARR">By default, all images in the PDF will be sized down to fit within your specified margin and page dimensions (see &#8220;<a href="{% post_url 2019-03-03-19-AdjustPDFtrimsizeandmargins %}" id="pgdEKuRkG"><span class="Hyperlink" id="pgojW1ICu">Adjust PDF trim size and margins</span></a>&#8221;). However, you may designate an image to be &#8220;full bleed&#8221;, which means that it will take up the entire page and extend into the bleed area beyond the page, creating a graphic that is flush with the edge of the book in the final product. To do so, you&#8217;ll need to use a process instruction (see &#8220;<a href="{% post_url 2019-03-03-22-Addspecialdesigninstructions %}" id="pKtDI5xWs"><span class="Hyperlink" id="pfsPRxn5R">Add special design instructions</span></a>&#8221;).</p>
    <ol class="hwprnum-liststart" data-hederis-type="hwprnum-liststart" id="p4oZBL9RI"><li class="hblkoli" data-hederis-type="hblkoli" id="liCeoyTKEw"><p class="hblkoli" data-hederis-type="hblkoli" id="pgY0XjOEI">In your Word manuscript, find the &#8220;HED Image holder&#8221; paragraph that contains your image filename.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="liFhxpHBzC"><p class="hblkoli" data-hederis-type="hblkoli" id="pIBkWdfRB">Insert a new paragraph below your image holder paragraph, and apply the &#8220;HED Processing instruction&#8221; style to it.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="liAQbjA8mG"><p class="hblkoli" data-hederis-type="hblkoli" id="pcX79BdRa">Type the following text inside your new HED Processing instruction paragraph: IMAGE-SIZE=fullbleed</p></li>
    </ol>
    <p class="hblkp" data-hederis-type="hblkp" id="pPqGx9Cza">Your Word manuscript should look like this:</p>
    <img data-hederis-type="hblkimg" class="hblkimg" id="p1pwzOtMp" src="/images/fullbleed-1.png"/>
    </section>
    