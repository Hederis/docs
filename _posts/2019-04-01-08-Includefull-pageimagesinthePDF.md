---
layout: default
title:  "Include full-page images in the PDF"
permalink:  /include-full-page-images/
categories: [Images]
published: true
---

<section data-type="chapter" class="hsecchapter" data-hederis-type="hsecchapter" id="include-full-page-images" data-pi-attrs="id: include-full-page-images"><h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="pqyY4RNsj">Include full-page images in the PDF</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="pBHN9MYfK">By default, all images in the PDF will be sized down to fit within your specified margin and page dimensions (see &#8220;<a href="{% post_url 2019-04-01-20-AdjustPDFtrimsizeandmargins %}"><span class="Hyperlink">Adjust PDF trim size and margins</span></a>&#8221;). However, you may designate an image to be &#8220;full bleed&#8221;, which means that it will take up the entire page and extend into the bleed area beyond the page, creating a graphic that is flush with the edge of the book in the final product. To do so, you&#8217;ll need to use a process instruction (see &#8220;<a href="{% post_url 2019-04-01-23-Addspeciallayoutinstructions %}"><span class="Hyperlink">Add special layout instructions</span></a>&#8221;).</p>
    <ol class="hwprnum-list" data-hederis-type="hwprnum-list" id="puPP39aTI"><li class="hblkoli" data-hederis-type="hblkoli" id="livH6MHkxU"><p class="hblkoli" data-hederis-type="hblkoli" id="pDGLZ2vI4">In your Word manuscript, find the &#8220;HED Image holder&#8221; paragraph that contains your image filename.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="li2ameSnRL"><p class="hblkoli" data-hederis-type="hblkoli" id="pbp6ILK1G">Insert a new paragraph below your image holder paragraph, and apply the &#8220;HED Processing instruction&#8221; style to it.</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="li8eUYmCCY"><p class="hblkoli" data-hederis-type="hblkoli" id="pDBp7zhY8">Type the following text inside your new HED Processing instruction paragraph: IMAGE-SIZE=fullbleed</p></li>
    </ol>
    <p class="hblkp" data-hederis-type="hblkp" id="pJYa3ROEb">Your Word manuscript should look like this:</p>
    <img data-hederis-type="hblkimg" class="hblkimg" id="pyJLuiBuJ" src="/images/fullbleed_1.png"/>
    </section>
    