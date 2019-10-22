---
layout: default
title:  "Customize the design of specific paragraphs, wrappers, or sections"
permalink:  /custom-paragraph-design/
categories: [Design]
tags: [convert]
published: true
---

<section data-type="chapter" class="hsecchapter" data-hederis-type="hsecchapter" id="custom-paragraph-design" data-pi-attrs="id: custom-paragraph-design; data-tags: convert;" role="doc-chapter" data-tags="convert" data-author-name=" " data-book-title=" " title="Customize the design of specific paragraphs, wrappers, or sections"><h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="pz2EOllC6">Customize the design of specific paragraphs, wrappers, or sections</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="pzdnXsYfj">You can use processing instructions (see &#8220;<a href="{% post_url 2019-10-21-35-Addspeciallayoutinstructions %}" id="psVft2QQk"><span class="Hyperlink" id="pJ0W65kS1">Add special layout instructions</span></a>&#8221;) to customize the design of individual paragraphs, wrappers, or sections in your manuscript. These design instructions are created with CSS, and will apply to both the PDF layout and the EPUB file. For the best results, make sure your CSS is valid, and add it without any extra line breaks or carriage returns (see the images below for examples). You can <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/Reference" id="pMEXkRaKj"><span class="Hyperlink" id="pRAiMOdnQ">learn more about CSS here</span></a>.</p>
    <p class="hblkp" data-hederis-type="hblkp" id="ptCqpZdEA">To customize a paragraph&#8217;s design:</p>
    <ol class="hwprnumlist" data-hederis-type="hwprnumlist" id="pIdD6amRi"><li class="hblkoli" data-hederis-type="hblkoli" id="liIETjrmy4"><p class="hblkoli" data-hederis-type="hblklip" id="pgmdbofbX">Find the paragraph that you want to customize, and insert a new HED Processing instruction paragraph below it (for more details on how to do this, see &#8220;<a href="{% post_url 2019-10-21-35-Addspeciallayoutinstructions %}" id="pAplAdg7o"><span class="Hyperlink" id="paI0td5rM">Add special layout instructions</span></a>&#8221;).</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="liuRLzBMGR"><p class="hblkoli" data-hederis-type="hblklip" id="ptepEPRly">In your processing instruction paragraph, type the text STYLE=, and then type the CSS that you want to apply to your paragraph.</p></li>
    </ol>
    <img data-hederis-type="hblkimg" class="hblkimg" id="p8xdiZnia" src="/images/pi2.png" data-img-src="pi2.png"/>
    <p class="hblkp" data-hederis-type="hblkp" id="pkqRvao5n">If you want to customize a wrapper, insert the processing instruction paragraph after <strong class="hspanstrong" data-hederis-type="hspanstrong" id="pdc6PjLtl">either</strong> the wrapper &#8220;start&#8221; or &#8220;end&#8221; paragraphs, as shown below: </p>
    <img data-hederis-type="hblkimg" class="hblkimg" id="phqedD0fi" src="/images/stylepiwrapper.png" data-img-src="stylepiwrapper.png"/>
    <p class="hblkp" data-hederis-type="hblkp" id="p6ObWyzo4">To customize an entire section, insert the processing instruction paragraph after the section start paragraph, as shown here:</p>
    <img data-hederis-type="hblkimg" class="hblkimg" id="p40CIAxsN" src="/images/stylepisection.png" data-img-src="stylepisection.png"/>
    <p class="hblkp" data-hederis-type="hblkp" id="pQUHuMPc0">Note that your custom design will be applied to both the PDF and EPUB formats, as best as possible, so you may need to include fallbacks in case a certain CSS value is supported in one format but not the other. One example of this is color spaces: while you may want to use CMYK colors in your PDF output, the CMYK color space is generally not supported in the EPUB format. To get around this, include a fallback, like this:</p>
    <img data-hederis-type="hblkimg" class="hblkimg" id="p4aGnKsax" src="/images/stylepicolorfallback.png" data-img-src="stylepicolorfallback.png"/>
    <p class="hblkp" data-hederis-type="hblkp" id="p52sbtNsx">Here, the layout engine will attempt to use the CMYK value first, and if it finds that it is not supported, it will fall back to the web value (which is supported on all web browsers and EPUB reading devices).</p>
    </section>
    