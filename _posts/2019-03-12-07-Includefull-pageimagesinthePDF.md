---
layout: default
title:  "Include full-page images in the PDF"
categories: [Images]
published: true
---

<section data-type="chapter" class="hsecchapter" data-hederis-type="hsecchapter" id="p5D8mx3q3"><h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="pQlbYTye9">Include full-page images in the PDF</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="pxxiRTNHH">By default, all images in the PDF will be sized down to fit within your specified margin and page dimensions (see &#8220;<a href="{% post_url 2019-03-12-19-AdjustPDFtrimsizeandmargins %}" id="p9bCJctGK"><span class="Hyperlink" id="pNpT1sUzV">Adjust PDF trim size and margins</span></a>&#8221;). However, you may designate an image to be &#8220;full bleed&#8221;, which means that it will take up the entire page and extend into the bleed area beyond the page, creating a graphic that is flush with the edge of the book in the final product. To do so, you&#8217;ll need to use a process instruction (see &#8220;<a href="{% post_url 2019-03-12-22-Addspecialdesigninstructions %}" id="pasptA6SY"><span class="Hyperlink" id="pjZLnRG0h">Add special design instructions</span></a>&#8221;).</p>
    <ol class="hwprnum-liststart" data-hederis-type="hwprnum-liststart" id="pMMyUy81v"><li class="hblkoli" data-hederis-type="hblkoli" id="lirmuO9Ehp"><p class="hblkoli" data-hederis-type="hblkoli" id="pcV5wFFbZ">In your Word manuscript, find the &#8220;HED Image holder&#8221; paragraph that contains your image filename.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="liddKYEQVg"><p class="hblkoli" data-hederis-type="hblkoli" id="pBZvW28Ra">Insert a new paragraph below your image holder paragraph, and apply the &#8220;HED Processing instruction&#8221; style to it.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="li8FYQbKhS"><p class="hblkoli" data-hederis-type="hblkoli" id="p8E9laqw9">Type the following text inside your new HED Processing instruction paragraph: IMAGE-SIZE=fullbleed</p></li>
    </ol>
    <p class="hblkp" data-hederis-type="hblkp" id="pSvrL97Aa">Your Word manuscript should look like this:</p>
    <img data-hederis-type="hblkimg" class="hblkimg" id="pJIRKIFBL" src="/images/fullbleed_1.png"/>
    </section>
    