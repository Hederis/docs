---
layout: default
title:  "Include full-page images in the PDF"
categories: [Images]
published: true
---

<section data-type="chapter" class="hsecchapter" data-hederis-type="hsecchapter" id="pCjaZeGk2"><h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="p3tyyHvfg">Include full-page images in the PDF</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="pC5rB4M1s">By default, all images in the PDF will be sized down to fit within your specified margin and page dimensions (see &#8220;<a href="{% post_url 2019-03-04-19-AdjustPDFtrimsizeandmargins %}" id="pijGKvFoY"><span class="Hyperlink" id="pujM2ydbM">Adjust PDF trim size and margins</span></a>&#8221;). However, you may designate an image to be &#8220;full bleed&#8221;, which means that it will take up the entire page and extend into the bleed area beyond the page, creating a graphic that is flush with the edge of the book in the final product. To do so, you&#8217;ll need to use a process instruction (see &#8220;<a href="{% post_url 2019-03-04-22-Addspecialdesigninstructions %}" id="pAHatbOgD"><span class="Hyperlink" id="pvCTjz9jm">Add special design instructions</span></a>&#8221;).</p>
    <ol class="hwprnum-liststart" data-hederis-type="hwprnum-liststart" id="pI9mkACYo"><li class="hblkoli" data-hederis-type="hblkoli" id="liN06bGJIb"><p class="hblkoli" data-hederis-type="hblkoli" id="pDRIa3msA">In your Word manuscript, find the &#8220;HED Image holder&#8221; paragraph that contains your image filename.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="lipLicVfgk"><p class="hblkoli" data-hederis-type="hblkoli" id="pswy6a9Aw">Insert a new paragraph below your image holder paragraph, and apply the &#8220;HED Processing instruction&#8221; style to it.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="linP041ekg"><p class="hblkoli" data-hederis-type="hblkoli" id="pFVX7YmKK">Type the following text inside your new HED Processing instruction paragraph: IMAGE-SIZE=fullbleed</p></li>
    </ol>
    <p class="hblkp" data-hederis-type="hblkp" id="pmnMTXfj1">Your Word manuscript should look like this:</p>
    <img data-hederis-type="hblkimg" class="hblkimg" id="pieZ5cLij" src="/images/fullbleed-1.png"/>
    </section>
    