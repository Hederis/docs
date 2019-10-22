---
layout: default
title:  "Add special layout instructions"
permalink:  /custom-design/
categories: [Design]
tags: [convert,typeset]
published: true
---

<section data-type="chapter" class="hsecchapter" data-hederis-type="hsecchapter" id="custom-design" data-pi-attrs="id: custom-design; data-tags: convert,typeset;" role="doc-chapter" data-tags="convert,typeset" data-author-name=" " data-book-title=" " title="Add special layout instructions"><h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="pDXB2ixVJ">Add special layout instructions</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="pZhuM0GHJ">You can tweak the design and layout of specific paragraphs, sections, or wrappers in your book by adding special instructions to your Word file, called <span class="Emphasis" id="pMMrMvKVL"><em class="hspanem" data-hederis-type="hspanem" id="pAruGg6KA">processing instructions</em></span>. We use processing instructions to convey a variety of different types of instructions: customizing running header content, adding CSS styles, adding attributes to the HTML, fixing image sizes, and more.</p>
    <p class="hblkp" data-hederis-type="hblkp" id="p8ShtCTai">After you&#8217;ve converted your manuscript for the first time, you&#8217;ll receive a new Word file with all of the special Hederis styles applied. (See &#8220;<a href="{% post_url 2019-10-21-16-Fine-tuneWordStyles %}" id="pYf5BTpaf"><span class="Hyperlink" id="p5MXW1WLL">Fine-tune Word Styles</span></a>&#8221; for more information on working with Word styles.) We have an extra style just for adding these design and layout instructions: &#8220;HED Processing instruction&#8221;.</p>
    <img data-hederis-type="hblkimg" class="hblkimg" id="pzKK7rnEg" src="/images/pi1.png" data-img-src="pi1.png"/>
    <p class="hblkp" data-hederis-type="hblkp" id="pQNe1bXbI">To add your processing instructions:</p>
    <ol class="hwprnumlist" data-hederis-type="hwprnumlist" id="pUkP4Uku4"><li class="hblkoli" data-hederis-type="hblkoli" id="liIWI9Y121"><p class="hblkoli" data-hederis-type="hblklip" id="pKCQBHGCW">Find the paragraph that you want to customize the design of, and insert a new paragraph after it (place your cursor at the end of the paragraph, and then press enter).</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="liBGyQH9tR"><p class="hblkoli" data-hederis-type="hblklip" id="py98JprsP">In your new paragraph, type the code for the type of instruction you&#8217;re adding, and then type an equals sign, and then type the code for the special design instruction. See the end of this section for a list of all of these codes. For example, if you want a paragraph to be centered instead of left-aligned, your text would look like this:</p><img data-hederis-type="hblkimg" class="hblkimg" id="p6yHViop4" src="/images/pi2.png" data-img-src="pi2.png"/>
    </li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="liusXUuqNS"><p class="hblkoli" data-hederis-type="hblklip" id="pmNWZsT81">Finally, make sure your cursor is still in the new paragraph, and then open the Styles pane. Scroll to find the HED Processing instruction style name and click on it; this will apply it to your new paragraph.</p></li>
    </ol>
    <p class="hblkp" data-hederis-type="hblkp" id="p6kuUf78X">You can apply a processing instruction to an entire section by inserting the processing instruction paragraph after the appropriate section start paragraph (see &#8220;<a href="{% post_url 2019-10-21-18-AddaSection %}" id="pJTLHIZxw"><span class="Hyperlink" id="pxZkrg9dD">Add a Section</span></a>&#8221;), and to a box by inserting the processing instruction paragraph after either the wrapper start or end paragraph (see &#8220;<a href="{% post_url 2019-10-21-17-AddaWrapper %}" id="pG1pnN7JU"><span class="Hyperlink" id="pHTgLjEgY">Add a Wrapper</span></a>&#8221;).</p>
    <aside class="hwprbox box" data-hederis-type="hwprbox" id="pmqVn9PoN" data-type="sidebar"><p class="hblktype" data-hederis-type="hblktype" id="pltQqt2bJ">Tip</p>
    <p class="hblkp" data-hederis-type="hblkp" id="pTfkgDTsd">If you don&#8217;t see the <span class="Emphasis" id="ptAuejC2a"><em class="hspanem" data-hederis-type="hspanem" id="pu2aVSOBH">HED Processing instruction</em></span> style in the Styles pane, try adjusting your Styles view options (see &#8220;<a href="{% post_url 2019-10-21-16-Fine-tuneWordStyles %}" id="pgDXHyv7v"><span class="Hyperlink" id="pKZgLhQwb">Fine-tune Word Styles</span></a>&#8221;).</p>
    </aside>
    <aside class="hwprbox box" data-hederis-type="hwprbox" id="pG4RfuFIt" data-type="sidebar"><p class="hblktype" data-hederis-type="hblktype" id="pOeRr7OJm">Tip</p>
    <p class="hblkp" data-hederis-type="hblkp" id="pZFVlHovM">You can make sure the style was applied by viewing your document in Draft View and expanding the Style area (see &#8220;<a href="{% post_url 2019-10-21-16-Fine-tuneWordStyles %}" id="pssnvVw0z"><span class="Hyperlink" id="prFacYzG6">Fine-tune Word Styles</span></a>&#8221;).</p>
    </aside>
    <aside class="hwprbox box" data-hederis-type="hwprbox" id="p0euIEZ33" data-type="sidebar"><p class="hblktype" data-hederis-type="hblktype" id="pVq5NCIHv">Tip</p>
    <p class="hblkp" data-hederis-type="hblkp" id="pKQ30ntiI">You can apply multiple types of processing instructions to a single paragraph by separating each option with a &#8220;+&#8221;, like this:</p>
    <img data-hederis-type="hblkimg" class="hblkimg" id="p9pFs2x0I" src="/images/pi3.png" data-img-src="pi3.png"/>
    </aside>
    <aside class="hwprbox box" data-hederis-type="hwprbox" id="pXTR5YQiR" data-type="sidebar"><p class="hblktype" data-hederis-type="hblktype" id="pFB8wSiWq">Tip</p>
    <p class="hblkp" data-hederis-type="hblkp" id="pN4qphaCC">Some processing instructions accept extra options that change their behavior. For example, the GLOBAL STYLE and ATTRS processing instructions can both accept the SCOPE-BODY option, which will apply your custom instruction to the entire document, rather than to just a single element or group of elements. See &#8220;<a href="{% post_url 2019-10-21-37-Customizethedesignofanentiregroupofparagraphswrappersorsections %}" id="pqKpxdDHu"><span class="Hyperlink" id="p0gpu01sN">Customize the design of an entire group of paragraphs, wrappers, or sections</span></a>&#8221; and &#8220;<a href="{% post_url 2019-10-21-46-AddcustomHTMLattributes %}" id="poTdcj1CD"><span class="Hyperlink" id="pn07NgdKa">Add custom HTML attributes</span></a>&#8221; for more info on how to do this.</p>
    </aside>
    <p class="hblkp" data-hederis-type="hblkp" id="peRIQOwGm">Processing Instruction codes:</p>
    <table id="pBIk2V2bW" data-hederis-type="hwprtable" class="hwprtable">
      <tr data-hederis-type="hwprtr" class="hwprtr" id="pCfXxlbNA">
        <td data-hederis-type="hwprtd" class="hwprtd" id="pVRDN8VNM">
          <p class="hblkp" data-hederis-type="hblkp" id="p2y9KD6NB"><strong class="hspanstrong" data-hederis-type="hspanstrong" id="porkGrhf3">Code</strong></p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="p0G3TVkpv">
          <p class="hblkp" data-hederis-type="hblkp" id="pcXrauP5i"><strong class="hspanstrong" data-hederis-type="hspanstrong" id="p60jE4b8c">Possible values</strong></p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="pgHASAFJo">
          <p class="hblkp" data-hederis-type="hblkp" id="pow7ojnsf"><strong class="hspanstrong" data-hederis-type="hspanstrong" id="ppAEmbvqI">Notes</strong></p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="p7KsaUZsk">
          <p class="hblkp" data-hederis-type="hblkp" id="p2rRbx9F5"><strong class="hspanstrong" data-hederis-type="hspanstrong" id="p38VUfKJr">Documentation</strong></p>
        </td>
      </tr>
      <tr data-hederis-type="hwprtr" class="hwprtr" id="pdFTcejXj">
        <td data-hederis-type="hwprtd" class="hwprtd" id="pHzAKsUp7">
          <p class="hblkp" data-hederis-type="hblkp" id="pij0iA9Hs">IMAGE-SIZE</p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="p0ZRihN5i">
          <p class="hblkp" data-hederis-type="hblkp" id="p5y69VY8R">fullbleed</p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="pC3Q7OLD8">
          <p class="hblkp" data-hederis-type="hblkp" id="p2EIyiQDK">In the print file, this will create a fullbleed image that will fill an entire page and bleed area. See Images for more info.</p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="pkn9JcHHy">
          <p class="hblkp" data-hederis-type="hblkp" id="pJhKKxrtw">See &#8220;<a href="{% post_url 2019-10-21-09-Includefull-pageimagesinthePDF %}" id="plCn16uBa"><span class="Hyperlink" id="pzk802Rrg">Include full-page images in the PDF</span></a>&#8221;</p>
        </td>
      </tr>
      <tr data-hederis-type="hwprtr" class="hwprtr" id="pVOSTqKhq">
        <td data-hederis-type="hwprtd" class="hwprtd" id="pAtSH6G7O">
          <p class="hblkp" data-hederis-type="hblkp" id="pnDQWxYbu">STYLE</p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="pF6ITpNVA">
          <p class="hblkp" data-hederis-type="hblkp" id="pNE9fRo2S">Any valid CSS property/value combination (<a href="https://developer.mozilla.org/en-US/docs/Web/CSS/Reference" id="popoAP0pd"><span class="Hyperlink" id="pjWgAvM4g">see this reference</span></a>)</p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="pvsMv0AK7"/>
        <td data-hederis-type="hwprtd" class="hwprtd" id="pJv8GLzUi">
          <p class="hblkp" data-hederis-type="hblkp" id="p8mr8Nc5M">See &#8220;<a href="{% post_url 2019-10-21-36-Customizethedesignofspecificparagraphswrappersorsections %}" id="pq62j98wJ"><span class="Hyperlink" id="phim6g3HF">Customize the design of specific paragraphs, wrappers, or sections</span></a>&#8221;</p>
        </td>
      </tr>
      <tr data-hederis-type="hwprtr" class="hwprtr" id="p12nNPtSB">
        <td data-hederis-type="hwprtd" class="hwprtd" id="pYJ7Qdj3q">
          <p class="hblkp" data-hederis-type="hblkp" id="pfutpC5fh">FORMAT</p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="pRmiakCxD">
          <p class="hblkp" data-hederis-type="hblkp" id="pamUAer9Y">ebook, print</p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="pHoyByp3H">
          <p class="hblkp" data-hederis-type="hblkp" id="pfk3b4WuV">Display a certain paragraph, wrapper, or section only in the ebook or PDF file. Default value is &#8220;both&#8221;.</p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="pxL4wfmLj">
          <p class="hblkp" data-hederis-type="hblkp" id="pUmV5v25w">See &#8220;<a href="{% post_url 2019-10-21-21-IncludecontentonlyinthePDForEPUB %}" id="pqwI08hJP"><span class="Hyperlink" id="pUDHxMbY6">Include content only in the PDF or EPUB</span></a>&#8221;</p>
        </td>
      </tr>
      <tr data-hederis-type="hwprtr" class="hwprtr" id="pNXCLaTh2">
        <td data-hederis-type="hwprtd" class="hwprtd" id="plA0wSvFq">
          <p class="hblkp" data-hederis-type="hblkp" id="pm0pYoHJb">GLOBAL STYLE</p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="pFBJ38hcZ">
          <p class="hblkp" data-hederis-type="hblkp" id="ppPxOQoe8">Any valid CSS property/value combination (<a href="https://developer.mozilla.org/en-US/docs/Web/CSS/Reference" id="pyyKagqmJ"><span class="Hyperlink" id="pOVvLPD1g">see this reference</span></a>). Also supports the &#8220;SCOPE-BODY&#8221; option.</p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="pppJODsns">
          <p class="hblkp" data-hederis-type="hblkp" id="pLvcDtEW5">To add custom design formatting to an entire group of elements (for example, to add a border around every extract in the entire book).</p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="pV1fiZf8E">
          <p class="hblkp" data-hederis-type="hblkp" id="pp3DqFxMU">See &#8220;<a href="{% post_url 2019-10-21-37-Customizethedesignofanentiregroupofparagraphswrappersorsections %}" id="parRIXB0c"><span class="Hyperlink" id="pIoSLBRHw">Customize the design of an entire group of paragraphs, wrappers, or sections</span></a>&#8221;</p>
        </td>
      </tr>
      <tr data-hederis-type="hwprtr" class="hwprtr" id="pY1RoHU1K">
        <td data-hederis-type="hwprtd" class="hwprtd" id="ptwqcm9D5">
          <p class="hblkp" data-hederis-type="hblkp" id="plr2itovt">ATTRS</p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="pt9XgyQcU">
          <p class="hblkp" data-hederis-type="hblkp" id="pe3z32fMx">The name and value of one or more <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes" id="pSm8KCyyj"><span class="Hyperlink" id="pCzIV6SJP">HTML attributes</span></a>. Multiple attributes should be separated by a semi-colon. Also supports the &#8220;SCOPE-BODY&#8221; option.</p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="pZqvNvFnz">
          <p class="hblkp" data-hederis-type="hblkp" id="pxiJLIXy5">You can use <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes" id="p6DskIPOM"><span class="Hyperlink" id="pYsc3HF2t">predefined HTML attributes</span></a>, or make up your own attributes that start with the &#8220;data-&#8221; prefix.</p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="pHtsQk4Zq">
          <p class="hblkp" data-hederis-type="hblkp" id="p5QTsp0Rj">See &#8220;<a href="{% post_url 2019-10-21-46-AddcustomHTMLattributes %}" id="pgYOmXXsQ"><span class="Hyperlink" id="pDZNGozE9">Add custom HTML attributes</span></a>&#8221;</p>
        </td>
      </tr>
    </table>
    <p class="hblkp" data-hederis-type="hblkp" id="py8JdDxb5">Have a suggestion for other types of instructions you might include? Email us! help@hederis.com</p>
    </section>
    