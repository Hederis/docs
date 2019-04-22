---
layout: default
title:  "Add special layout instructions"
permalink:  /custom-design/
categories: [Design]
published: true
---

<section data-type="chapter" class="hsecchapter" data-hederis-type="hsecchapter" id="custom-design" data-pi-attrs="id: custom-design" role="doc-chapter"><h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="prcPxgl1v">Add special layout instructions</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="pmYRUq0tu">You can tweak the design and layout of specific paragraphs, sections, or wrappers in your book by adding special instructions to your Word file, called <em>processing instructions</em>.</p>
    <p class="hblkp" data-hederis-type="hblkp" id="pgwWKN0na">After you&#8217;ve converted your manuscript for the first time, you&#8217;ll receive a new Word file with all of the special Hederis styles applied. (See &#8220;<a href="{% post_url 2019-04-22-14-Fine-tuneWordStyles %}"><span class="Hyperlink">Fine-tune Word Styles</span></a>&#8221; for more information on working with Word styles.) We have an extra style just for adding these design and layout instructions: &#8220;HED Processing instruction&#8221;.</p>
    <img data-hederis-type="hblkimg" class="hblkimg" id="pqExkGAOK" src="/images/pi1.png"/>
    <p class="hblkp" data-hederis-type="hblkp" id="pMznrPERC">To add your processing instructions:</p>
    <ol class="hwprnum-list" data-hederis-type="hwprnum-list" id="pEU3qUh9b"><li class="hblkoli" data-hederis-type="hblkoli" id="liqRpY4Euw"><p class="hblkoli" data-hederis-type="hblkoli" id="pLnnYFZUX">Find the paragraph that you want to customize the design of, and insert a new paragraph after it (place your cursor at the end of the paragraph, and then press enter).</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="liZMJHXMWI"><p class="hblkoli" data-hederis-type="hblkoli" id="pyOHLJCiE">In your new paragraph, type the code for the type of instruction you&#8217;re adding, and then type an equals sign, and then type the code for the special design instruction. See the end of this section for a list of all of these codes. For example, if you want a paragraph to be centered instead of left-aligned, your text would look like this:</p><img data-hederis-type="hblkimg" class="hblkimg" id="p64jo73zS" src="/images/pi2.png"/>
    </li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="li2GeP8gID"><p class="hblkoli" data-hederis-type="hblkoli" id="p4kP6nbFu">Finally, make sure your cursor is still in the new paragraph, and then open the Styles pane. Scroll to find the HED Processing instruction style name and click on it; this will apply it to your new paragraph.</p></li>
    </ol>
    <p class="hblkp" data-hederis-type="hblkp" id="pCeNJPB1R">You can apply a processing instruction to an entire section by inserting the processing instruction paragraph after the appropriate section start paragraph (see &#8220;<a href="{% post_url 2019-04-22-16-AddaSection %}"><span class="Hyperlink">Add a Section</span></a>&#8221;), and to a box by inserting the processing instruction paragraph after either the wrapper start or end paragraph (see &#8220;<a href="{% post_url 2019-04-22-15-AddaWrapper %}"><span class="Hyperlink">Add a Wrapper</span></a>&#8221;).</p>
    <aside class="hwprbox box" data-hederis-type="hwprbox" id="puUtu6l6A" data-type="sidebar"><p class="hblktype" data-hederis-type="hblktype" id="poE7aBxqg">Tip</p>
    <p class="hblkp" data-hederis-type="hblkp" id="pHeGqiDxm">If you don&#8217;t see the <em>HED Processing instruction</em> style in the Styles pane, try adjusting your Styles view options (see &#8220;<a href="{% post_url 2019-04-22-14-Fine-tuneWordStyles %}"><span class="Hyperlink">Fine-tune Word Styles</span></a>&#8221;).</p>
    </aside>
    <aside class="hwprbox box" data-hederis-type="hwprbox" id="pYYApb87t" data-type="sidebar"><p class="hblktype" data-hederis-type="hblktype" id="pp9gWfNqb">Tip</p>
    <p class="hblkp" data-hederis-type="hblkp" id="pHzQ8g8aK">You can make sure the style was applied by viewing your document in Draft View and expanding the Style area (see &#8220;<a href="{% post_url 2019-04-22-14-Fine-tuneWordStyles %}"><span class="Hyperlink">Fine-tune Word Styles</span></a>&#8221;).</p>
    </aside>
    <aside class="hwprbox box" data-hederis-type="hwprbox" id="pzNiNJQ9X" data-type="sidebar"><p class="hblktype" data-hederis-type="hblktype" id="pIfE9Eh6B">Tip</p>
    <p class="hblkp" data-hederis-type="hblkp" id="pXE1iNMor">You can apply multiple types of processing instructions to a single paragraph by separating each option with a &#8220;+&#8221;, like this:</p>
    <img data-hederis-type="hblkimg" class="hblkimg" id="ply7qnzX3" src="/images/pi3.png"/>
    </aside>
    <aside class="hwprbox box" data-hederis-type="hwprbox" id="paeuMJnoW" data-type="sidebar"><p class="hblktype" data-hederis-type="hblktype" id="pPUzPatbq">Tip</p>
    <p class="hblkp" data-hederis-type="hblkp" id="pLTDr3qKg">Some processing instructions accept extra options that change their behavior. For example, the GLOBAL STYLE and ATTRS processing instructions can both accept the SCOPE-BODY option, which will apply your custom instruction to the entire document, rather than to just a single element or group of elements. See &#8220;<a href="{% post_url 2019-04-22-26-Customizethedesignofanentiregroupofparagraphswrappersorsections %}"><span class="Hyperlink">Customize the design of an entire group of paragraphs, wrappers, or sections</span></a>&#8221; and &#8220;<a href="{% post_url 2019-04-22-28-AddcustomHTMLattributes %}"><span class="Hyperlink">Add custom HTML attributes</span></a>&#8221; for more info on how to do this.</p>
    </aside>
    <p class="hblkp" data-hederis-type="hblkp" id="pYtlpnl5K">Processing Instruction codes:</p>
    <table id="pgQVBt2lX">
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
          <p class="hblkp" data-hederis-type="hblkp">See &#8220;<a href="{% post_url 2019-04-22-08-Includefull-pageimagesinthePDF %}"><span class="Hyperlink">Include full-page images in the PDF</span></a>&#8221;</p>
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
          <p class="hblkp" data-hederis-type="hblkp">See &#8220;<a href="{% post_url 2019-04-22-25-Customizethedesignofspecificparagraphswrappersorsections %}"><span class="Hyperlink">Customize the design of specific paragraphs, wrappers, or sections</span></a>&#8221;</p>
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
          <p class="hblkp" data-hederis-type="hblkp">See &#8220;<a href="{% post_url 2019-04-22-18-IncludecontentonlyinthePDForEPUB %}"><span class="Hyperlink">Include content only in the PDF or EPUB</span></a>&#8221;</p>
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
          <p class="hblkp" data-hederis-type="hblkp">See &#8220;<a href="{% post_url 2019-04-22-26-Customizethedesignofanentiregroupofparagraphswrappersorsections %}"><span class="Hyperlink">Customize the design of an entire group of paragraphs, wrappers, or sections</span></a>&#8221;</p>
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
          <p class="hblkp" data-hederis-type="hblkp">See &#8220;<a href="{% post_url 2019-04-22-28-AddcustomHTMLattributes %}"><span class="Hyperlink">Add custom HTML attributes</span></a>&#8221;</p>
        </td>
      </tr>
    </table>
    <p class="hblkp" data-hederis-type="hblkp" id="pPMZiTwbh">Have a suggestion for other types of instructions you might include? Email us! help@hederis.com</p>
    </section>
    