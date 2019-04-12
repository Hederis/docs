---
layout: default
title:  "Add special layout instructions"
permalink:  /custom-design/
categories: [Design]
published: true
---

<section data-type="chapter" class="hsecchapter" data-hederis-type="hsecchapter" id="custom-design" data-pi-attrs="id: custom-design" role="doc-chapter"><h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="pyfrDF2m1">Add special layout instructions</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="pRdwXz2pJ">You can tweak the design and layout of specific paragraphs, sections, or wrappers in your book by adding special instructions to your Word file, called <em>processing instructions</em>.</p>
    <p class="hblkp" data-hederis-type="hblkp" id="p4pjnzq2d">After you&#8217;ve converted your manuscript for the first time, you&#8217;ll receive a new Word file with all of the special Hederis styles applied. (See &#8220;<a href="{% post_url 2019-04-12-14-Fine-tuneWordStyles %}"><span class="Hyperlink">Fine-tune Word Styles</span></a>&#8221; for more information on working with Word styles.) We have an extra style just for adding these design and layout instructions: &#8220;HED Processing instruction&#8221;.</p>
    <img data-hederis-type="hblkimg" class="hblkimg" id="p3ZFbahXs" src="/images/pi1.png"/>
    <p class="hblkp" data-hederis-type="hblkp" id="pvSBCgwBs">To add your processing instructions:</p>
    <ol class="hwprnum-list" data-hederis-type="hwprnum-list" id="pYR5bu1fh"><li class="hblkoli" data-hederis-type="hblkoli" id="likQW5vp83"><p class="hblkoli" data-hederis-type="hblkoli" id="pII9OJmT4">Find the paragraph that you want to customize the design of, and insert a new paragraph after it (place your cursor at the end of the paragraph, and then press enter).</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="liex68k0pu"><p class="hblkoli" data-hederis-type="hblkoli" id="pYp3oEllx">In your new paragraph, type the code for the type of instruction you&#8217;re adding, and then type an equals sign, and then type the code for the special design instruction. See the end of this section for a list of all of these codes. For example, if you want a paragraph to be centered instead of left-aligned, your text would look like this:</p><img data-hederis-type="hblkimg" class="hblkimg" id="pE0ougItK" src="/images/pi2.png"/>
    </li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="li5stzit7V"><p class="hblkoli" data-hederis-type="hblkoli" id="pk7dPuWNN">Finally, make sure your cursor is still in the new paragraph, and then open the Styles pane. Scroll to find the HED Processing instruction style name and click on it; this will apply it to your new paragraph.</p></li>
    </ol>
    <p class="hblkp" data-hederis-type="hblkp" id="pb4Vvdgaw">You can apply a processing instruction to an entire section by inserting the processing instruction paragraph after the appropriate section start paragraph (see &#8220;<a href="{% post_url 2019-04-12-16-AddaSection %}"><span class="Hyperlink">Add a Section</span></a>&#8221;), and to a box by inserting the processing instruction paragraph after either the wrapper start or end paragraph (see &#8220;<a href="{% post_url 2019-04-12-15-AddaWrapper %}"><span class="Hyperlink">Add a Wrapper</span></a>&#8221;).</p>
    <aside class="hwprbox box" data-hederis-type="hwprbox" id="pLk0I5841" data-type="sidebar"><p class="hblktype" data-hederis-type="hblktype" id="p3fJ2KBwO">Tip</p>
    <p class="hblkp" data-hederis-type="hblkp" id="pFOSAkbt2">If you don&#8217;t see the <em>HED Processing instruction</em> style in the Styles pane, try adjusting your Styles view options (see &#8220;<a href="{% post_url 2019-04-12-14-Fine-tuneWordStyles %}"><span class="Hyperlink">Fine-tune Word Styles</span></a>&#8221;).</p>
    </aside>
    <aside class="hwprbox box" data-hederis-type="hwprbox" id="p4hbYZgRT" data-type="sidebar"><p class="hblktype" data-hederis-type="hblktype" id="pNncH0quf">Tip</p>
    <p class="hblkp" data-hederis-type="hblkp" id="prTkbOdfB">You can make sure the style was applied by viewing your document in Draft View and expanding the Style area (see &#8220;<a href="{% post_url 2019-04-12-14-Fine-tuneWordStyles %}"><span class="Hyperlink">Fine-tune Word Styles</span></a>&#8221;).</p>
    </aside>
    <aside class="hwprbox box" data-hederis-type="hwprbox" id="pFib7drs5" data-type="sidebar"><p class="hblktype" data-hederis-type="hblktype" id="pqcl5v8TT">Tip</p>
    <p class="hblkp" data-hederis-type="hblkp" id="phmbamEFb">You can apply multiple types of processing instructions to a single paragraph by separating each option with a &#8220;+&#8221;, like this:</p>
    <img data-hederis-type="hblkimg" class="hblkimg" id="p438nc1De" src="/images/pi3.png"/>
    </aside>
    <aside class="hwprbox box" data-hederis-type="hwprbox" id="plQic2asv" data-type="sidebar"><p class="hblktype" data-hederis-type="hblktype" id="phMhZG44r">Tip</p>
    <p class="hblkp" data-hederis-type="hblkp" id="p8JjTdtwJ">Some processing instructions accept extra options that change their behavior. For example, the GLOBAL STYLE and ATTRS processing instructions can both accept the SCOPE-BODY option, which will apply your custom instruction to the entire document, rather than to just a single element or group of elements. See &#8220;<a href="{% post_url 2019-04-12-26-Customizethedesignofanentiregroupofparagraphswrappersorsections %}"><span class="Hyperlink">Customize the design of an entire group of paragraphs, wrappers, or sections</span></a>&#8221; and &#8220;<a href="{% post_url 2019-04-12-28-AddcustomHTMLattributes %}"><span class="Hyperlink">Add custom HTML attributes</span></a>&#8221; for more info on how to do this.</p>
    </aside>
    <p class="hblkp" data-hederis-type="hblkp" id="pfQWUnQMU">Processing Instruction codes:</p>
    <table id="pJNgeyYBB">
      <tr>
        <td>
          <p class="hblkp" data-hederis-type="hblkp"><strong>Code</strong></p>
        </td>
        <td>
          <p class="hblkp" data-hederis-type="hblkp"><strong>Possible values</strong></p>
        </td>
        <td>
          <p class="hblkp" data-hederis-type="hblkp"><strong>Notes</strong></p>
        </td>
        <td>
          <p class="hblkp" data-hederis-type="hblkp"><strong>Documentation</strong></p>
        </td>
      </tr>
      <tr>
        <td>
          <p class="hblkp" data-hederis-type="hblkp">IMAGE-SIZE</p>
        </td>
        <td>
          <p class="hblkp" data-hederis-type="hblkp">fullbleed</p>
        </td>
        <td>
          <p class="hblkp" data-hederis-type="hblkp">In the print file, this will create a fullbleed image that will fill an entire page and bleed area. See Images for more info.</p>
        </td>
        <td>
          <p class="hblkp" data-hederis-type="hblkp">See &#8220;<a href="{% post_url 2019-04-12-08-Includefull-pageimagesinthePDF %}"><span class="Hyperlink">Include full-page images in the PDF</span></a>&#8221;</p>
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
          <p class="hblkp" data-hederis-type="hblkp">See &#8220;<a href="{% post_url 2019-04-12-25-Customizethedesignofspecificparagraphswrappersorsections %}"><span class="Hyperlink">Customize the design of specific paragraphs, wrappers, or sections</span></a>&#8221;</p>
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
          <p class="hblkp" data-hederis-type="hblkp">See &#8220;<a href="{% post_url 2019-04-12-18-IncludecontentonlyinthePDForEPUB %}"><span class="Hyperlink">Include content only in the PDF or EPUB</span></a>&#8221;</p>
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
          <p class="hblkp" data-hederis-type="hblkp">See &#8220;<a href="{% post_url 2019-04-12-26-Customizethedesignofanentiregroupofparagraphswrappersorsections %}"><span class="Hyperlink">Customize the design of an entire group of paragraphs, wrappers, or sections</span></a>&#8221;</p>
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
          <p class="hblkp" data-hederis-type="hblkp">See &#8220;<a href="{% post_url 2019-04-12-28-AddcustomHTMLattributes %}"><span class="Hyperlink">Add custom HTML attributes</span></a>&#8221;</p>
        </td>
      </tr>
    </table>
    <p class="hblkp" data-hederis-type="hblkp" id="p39YW5lKg">Have a suggestion for other types of instructions you might include? Email us! help@hederis.com</p>
    </section>
    