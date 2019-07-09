---
layout: default
title:  "Add special layout instructions"
permalink:  /custom-design/
categories: [Design]
tags: [convert,typeset]
published: true
---

<section data-type="chapter" class="hsecchapter" data-hederis-type="hsecchapter" id="custom-design" data-pi-attrs="id: custom-design; data-tags: convert,typeset;" role="doc-chapter" data-tags="convert,typeset" data-author-name=" " data-book-title=" " title="Add special layout instructions"><h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="p5mD07fx8">Add special layout instructions</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="p64UVbY4B">You can tweak the design and layout of specific paragraphs, sections, or wrappers in your book by adding special instructions to your Word file, called <em data-hederis-type="hspanem">processing instructions</em>. We use processing instructions to convey a variety of different types of instructions: customizing running header content, adding CSS styles, adding attributes to the HTML, fixing image sizes, and more.</p>
    <p class="hblkp" data-hederis-type="hblkp" id="p8qH9m1cQ">After you&#8217;ve converted your manuscript for the first time, you&#8217;ll receive a new Word file with all of the special Hederis styles applied. (See &#8220;<a href="{% post_url 2019-07-09-15-Fine-tuneWordStyles %}"><span class="Hyperlink">Fine-tune Word Styles</span></a>&#8221; for more information on working with Word styles.) We have an extra style just for adding these design and layout instructions: &#8220;HED Processing instruction&#8221;.</p>
    <img data-hederis-type="hblkimg" class="hblkimg" id="pIhE3RNKT" src="/images/pi1.png"/>
    <p class="hblkp" data-hederis-type="hblkp" id="pDBgi2hgK">To add your processing instructions:</p>
    <ol class="hwprnum-list" data-hederis-type="hwprnum-list" id="pAb5CVkNE"><li class="hblkoli" data-hederis-type="hblkoli" id="li3t4s8Hzi"><p class="hblkoli" data-hederis-type="hblkoli" id="phCBV2FJ5">Find the paragraph that you want to customize the design of, and insert a new paragraph after it (place your cursor at the end of the paragraph, and then press enter).</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="ligthEtcFV"><p class="hblkoli" data-hederis-type="hblkoli" id="pLBBZXDjv">In your new paragraph, type the code for the type of instruction you&#8217;re adding, and then type an equals sign, and then type the code for the special design instruction. See the end of this section for a list of all of these codes. For example, if you want a paragraph to be centered instead of left-aligned, your text would look like this:</p><img data-hederis-type="hblkimg" class="hblkimg" id="pEyNuv0KO" src="/images/pi2.png"/>
    </li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="li9k2pf0NV"><p class="hblkoli" data-hederis-type="hblkoli" id="px0F6Yedo">Finally, make sure your cursor is still in the new paragraph, and then open the Styles pane. Scroll to find the HED Processing instruction style name and click on it; this will apply it to your new paragraph.</p></li>
    </ol>
    <p class="hblkp" data-hederis-type="hblkp" id="pAH9vMjKw">You can apply a processing instruction to an entire section by inserting the processing instruction paragraph after the appropriate section start paragraph (see &#8220;<a href="{% post_url 2019-07-09-17-AddaSection %}"><span class="Hyperlink">Add a Section</span></a>&#8221;), and to a box by inserting the processing instruction paragraph after either the wrapper start or end paragraph (see &#8220;<a href="{% post_url 2019-07-09-16-AddaWrapper %}"><span class="Hyperlink">Add a Wrapper</span></a>&#8221;).</p>
    <aside class="hwprbox box" data-hederis-type="hwprbox" id="p0fDNfSbL" data-type="sidebar"><p class="hblktype" data-hederis-type="hblktype" id="pfIXqwwWL">Tip</p>
    <p class="hblkp" data-hederis-type="hblkp" id="pL55WQ5Hm">If you don&#8217;t see the <em data-hederis-type="hspanem">HED Processing instruction</em> style in the Styles pane, try adjusting your Styles view options (see &#8220;<a href="{% post_url 2019-07-09-15-Fine-tuneWordStyles %}"><span class="Hyperlink">Fine-tune Word Styles</span></a>&#8221;).</p>
    </aside>
    <aside class="hwprbox box" data-hederis-type="hwprbox" id="pTC1aO5i9" data-type="sidebar"><p class="hblktype" data-hederis-type="hblktype" id="p4oRfLuq6">Tip</p>
    <p class="hblkp" data-hederis-type="hblkp" id="psdLNFQvp">You can make sure the style was applied by viewing your document in Draft View and expanding the Style area (see &#8220;<a href="{% post_url 2019-07-09-15-Fine-tuneWordStyles %}"><span class="Hyperlink">Fine-tune Word Styles</span></a>&#8221;).</p>
    </aside>
    <aside class="hwprbox box" data-hederis-type="hwprbox" id="pd976hgN5" data-type="sidebar"><p class="hblktype" data-hederis-type="hblktype" id="ph9t3ADnh">Tip</p>
    <p class="hblkp" data-hederis-type="hblkp" id="p4vyvSbbG">You can apply multiple types of processing instructions to a single paragraph by separating each option with a &#8220;+&#8221;, like this:</p>
    <img data-hederis-type="hblkimg" class="hblkimg" id="pu9UWkW6E" src="/images/pi3.png"/>
    </aside>
    <aside class="hwprbox box" data-hederis-type="hwprbox" id="pqQDRZWrh" data-type="sidebar"><p class="hblktype" data-hederis-type="hblktype" id="pBY5bc9WB">Tip</p>
    <p class="hblkp" data-hederis-type="hblkp" id="pwOxBJaSJ">Some processing instructions accept extra options that change their behavior. For example, the GLOBAL STYLE and ATTRS processing instructions can both accept the SCOPE-BODY option, which will apply your custom instruction to the entire document, rather than to just a single element or group of elements. See &#8220;<a href="{% post_url 2019-07-09-34-Customizethedesignofanentiregroupofparagraphswrappersorsections %}"><span class="Hyperlink">Customize the design of an entire group of paragraphs, wrappers, or sections</span></a>&#8221; and &#8220;<a href="{% post_url 2019-07-09-43-AddcustomHTMLattributes %}"><span class="Hyperlink">Add custom HTML attributes</span></a>&#8221; for more info on how to do this.</p>
    </aside>
    <p class="hblkp" data-hederis-type="hblkp" id="pPniWt0XY">Processing Instruction codes:</p>
    <table id="pJBKnnvxq">
      <tr>
        <td>
          <h1 data-hederis-type="hblkchaptitle" class="hblkp"><strong data-hederis-type="hspanstrong">Code</strong></h1>
        </td>
        <td>
          <p class="hblkp" data-hederis-type="hblkpostscript"><strong data-hederis-type="hspanstrong">Possible values</strong></p>
        </td>
        <td>
          <h1 data-hederis-type="hblkchaptitle" class="hblkp"><strong data-hederis-type="hspanstrong">Notes</strong></h1>
        </td>
        <td>
          <h2 data-hederis-type="hblksubtitle" class="hblkp" role="doc-subtitle"><strong data-hederis-type="hspanstrong">Documentation</strong></h2>
        </td>
      </tr>
      <tr>
        <td>
          <h2 data-hederis-type="hblksubtitle" class="hblkp" role="doc-subtitle">IMAGE-SIZE</h2>
        </td>
        <td>
          <h2 data-hederis-type="hblksubtitle" class="hblkp" role="doc-subtitle">fullbleed</h2>
        </td>
        <td>
          <p class="hblkp" data-hederis-type="hblkp">In the print file, this will create a fullbleed image that will fill an entire page and bleed area. See Images for more info.</p>
        </td>
        <td>
          <p class="hblkp" data-hederis-type="hblkp">See &#8220;<a href="{% post_url 2019-07-09-09-Includefull-pageimagesinthePDF %}"><span class="Hyperlink">Include full-page images in the PDF</span></a>&#8221;</p>
        </td>
      </tr>
      <tr>
        <td>
          <p class="hblkp" data-hederis-type="hblkp">STYLE</p>
        </td>
        <td>
          <p class="hblkp" data-hederis-type="hblkp">Any valid CSS property/value combination (<a href="https://developer.mozilla.org/en-US/docs/Web/CSS/Reference"><span class="Hyperlink">see this reference</span></a>)</p>
        </td>
        <td/>
        <td>
          <p class="hblkp" data-hederis-type="hblkp">See &#8220;<a href="{% post_url 2019-07-09-33-Customizethedesignofspecificparagraphswrappersorsections %}"><span class="Hyperlink">Customize the design of specific paragraphs, wrappers, or sections</span></a>&#8221;</p>
        </td>
      </tr>
      <tr>
        <td>
          <p class="hblkp" data-hederis-type="hblkp">FORMAT</p>
        </td>
        <td>
          <p class="hblkp" data-hederis-type="hblkp">ebook, print</p>
        </td>
        <td>
          <p class="hblkp" data-hederis-type="hblkp">Display a certain paragraph, wrapper, or section only in the ebook or PDF file. Default value is &#8220;both&#8221;.</p>
        </td>
        <td>
          <p class="hblkp" data-hederis-type="hblkp">See &#8220;<a href="{% post_url 2019-07-09-20-IncludecontentonlyinthePDForEPUB %}"><span class="Hyperlink">Include content only in the PDF or EPUB</span></a>&#8221;</p>
        </td>
      </tr>
      <tr>
        <td>
          <p class="hblkp" data-hederis-type="hblkp">GLOBAL STYLE</p>
        </td>
        <td>
          <p class="hblkp" data-hederis-type="hblkp">Any valid CSS property/value combination (<a href="https://developer.mozilla.org/en-US/docs/Web/CSS/Reference"><span class="Hyperlink">see this reference</span></a>). Also supports the &#8220;SCOPE-BODY&#8221; option.</p>
        </td>
        <td>
          <p class="hblkp" data-hederis-type="hblkp">To add custom design formatting to an entire group of elements (for example, to add a border around every extract in the entire book).</p>
        </td>
        <td>
          <p class="hblkp" data-hederis-type="hblkp">See &#8220;<a href="{% post_url 2019-07-09-34-Customizethedesignofanentiregroupofparagraphswrappersorsections %}"><span class="Hyperlink">Customize the design of an entire group of paragraphs, wrappers, or sections</span></a>&#8221;</p>
        </td>
      </tr>
      <tr>
        <td>
          <p class="hblkp" data-hederis-type="hblkp">ATTRS</p>
        </td>
        <td>
          <p class="hblkp" data-hederis-type="hblkp">The name and value of one or more <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes"><span class="Hyperlink">HTML attributes</span></a>. Multiple attributes should be separated by a semi-colon. Also supports the &#8220;SCOPE-BODY&#8221; option.</p>
        </td>
        <td>
          <p class="hblkp" data-hederis-type="hblkp">You can use <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes"><span class="Hyperlink">predefined HTML attributes</span></a>, or make up your own attributes that start with the &#8220;data-&#8221; prefix.</p>
        </td>
        <td>
          <p class="hblkp" data-hederis-type="hblkp">See &#8220;<a href="{% post_url 2019-07-09-43-AddcustomHTMLattributes %}"><span class="Hyperlink">Add custom HTML attributes</span></a>&#8221;</p>
        </td>
      </tr>
    </table>
    <p class="hblkp" data-hederis-type="hblkp" id="pF925LOZ6">Have a suggestion for other types of instructions you might include? Email us! help@hederis.com</p>
    </section>
    