---
layout: default
title:  "Customize the design of specific paragraphs, wrappers, or sections"
permalink:  /custom-paragraph-design/
categories: [Design]
published: true
---

<section data-type="chapter" class="hsecchapter" data-hederis-type="hsecchapter" id="custom-paragraph-design" data-pi-attrs="id: custom-paragraph-design"><h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="pLlJt7Lhx">Customize the design of specific paragraphs, wrappers, or sections</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="pnuL56iLH">You can use processing instructions (see &#8220;<a href="{% post_url 2019-04-01-23-Addspeciallayoutinstructions %}"><span class="Hyperlink">Add special layout instructions</span></a>&#8221;) to customize the design of individual paragraphs, wrappers, or sections in your manuscript. These design instructions are created with CSS, and will apply to both the PDF layout and the EPUB file. For the best results, make sure your CSS is valid, and add it without any extra line breaks or carriage returns (see the images below for examples). You can <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/Reference"><span class="Hyperlink">learn more about CSS here</span></a>.</p>
    <p class="hblkp" data-hederis-type="hblkp" id="pZrkUDW43">To customize a paragraph&#8217;s design:</p>
    <ol class="hwprnum-list" data-hederis-type="hwprnum-list" id="p1v2evTtl"><li class="hblkoli" data-hederis-type="hblkoli" id="linUXE5jvz"><p class="hblkoli" data-hederis-type="hblkoli" id="phQErExnM">Find the paragraph that you want to customize, and insert a new HED Processing instruction paragraph below it (for more details on how to do this, see &#8220;<a href="{% post_url 2019-04-01-23-Addspeciallayoutinstructions %}"><span class="Hyperlink">Add special layout instructions</span></a>&#8221;).</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="lizaPSpgoB"><p class="hblkoli" data-hederis-type="hblkoli" id="plci95FeZ">In your processing instruction paragraph, type the text STYLE=, and then type the CSS that you want to apply to your paragraph.</p></li>
    </ol>
    <img data-hederis-type="hblkimg" class="hblkimg" id="p29lIaIZc" src="/images/pi2.png"/>
    <p class="hblkp" data-hederis-type="hblkp" id="p8YBT5Eo9">If you want to customize a wrapper, insert the processing instruction paragraph after <strong>either</strong> the wrapper &#8220;start&#8221; or &#8220;end&#8221; paragraphs, as shown below: </p>
    <img data-hederis-type="hblkimg" class="hblkimg" id="p56ewYMUx" src="/images/stylepiwrapper.png"/>
    <p class="hblkp" data-hederis-type="hblkp" id="p3Jtr1DJM">To customize an entire section, insert the processing instruction paragraph after the section start paragraph, as shown here:</p>
    <img data-hederis-type="hblkimg" class="hblkimg" id="p2GK0LMvz" src="/images/stylepisection.png"/>
    <p class="hblkp" data-hederis-type="hblkp" id="prlYD5BgW">Note that your custom design will be applied to both the PDF and EPUB formats, as best as possible, so you may need to include fallbacks in case a certain CSS value is supported in one format but not the other. One example of this is color spaces: while you may want to use CMYK colors in your PDF output, the CMYK color space is generally not supported in the EPUB format. To get around this, include a fallback, like this:</p>
    <img data-hederis-type="hblkimg" class="hblkimg" id="pBaba7q9n" src="/images/stylepicolorfallback.png"/>
    <p class="hblkp" data-hederis-type="hblkp" id="pnPTLShxU">Here, the layout engine will attempt to use the CMYK value first, and if it finds that it is not supported, it will fall back to the web value (which is supported on all web browsers and EPUB reading devices).</p>
    </section>
    