---
layout: default
title:  "Add special layout instructions"
permalink:  /custom-design/
categories: [Design]
tags: [convert,typeset]
published: true
---

<section data-type="chapter" class="hsecchapter" data-hederis-type="hsecchapter" id="custom-design" data-pi-attrs="id: custom-design; data-tags: convert,typeset;" role="doc-chapter" data-tags="convert,typeset" data-author-name=" " data-book-title=" " title="Add special layout instructions"><h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="pM4PyeGAj">Add special layout instructions</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="pGpRDNW5z">You can tweak the design and layout of specific paragraphs, sections, or wrappers in your book by adding special instructions to your Word file, called <span class="Emphasis" id="pYKdpB5Sh"><em class="hspanem" data-hederis-type="hspanem" id="plYBPzaiK">processing instructions</em></span>. We use processing instructions to convey a variety of different types of instructions: customizing running header content, adding CSS styles, adding attributes to the HTML, fixing image sizes, and more.</p>
    <p class="hblkp" data-hederis-type="hblkp" id="ps53NFpWw">After you&#8217;ve converted your manuscript for the first time, you&#8217;ll receive a new Word file with all of the special Hederis styles applied. (See &#8220;<a href="{% post_url 2019-10-21-16-Fine-tuneWordStyles %}" id="pMa3WvYzR"><span class="Hyperlink" id="pEPIsePkP">Fine-tune Word Styles</span></a>&#8221; for more information on working with Word styles.) We have an extra style just for adding these design and layout instructions: &#8220;HED Processing instruction&#8221;.</p>
    <img data-hederis-type="hblkimg" class="hblkimg" id="pcPrUOGsg" src="/images/pi1.png" data-img-src="pi1.png"/>
    <p class="hblkp" data-hederis-type="hblkp" id="p4j1hTy8u">To add your processing instructions:</p>
    <ol class="hwprnumlist" data-hederis-type="hwprnumlist" id="pI0woLFzX"><li class="hblkoli" data-hederis-type="hblkoli" id="lip5sHxZ7h"><p class="hblkoli" data-hederis-type="hblklip" id="pXZnSfKad">Find the paragraph that you want to customize the design of, and insert a new paragraph after it (place your cursor at the end of the paragraph, and then press enter).</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="liTnil2yGk"><p class="hblkoli" data-hederis-type="hblklip" id="pDD2hAW7x">In your new paragraph, type the code for the type of instruction you&#8217;re adding, and then type an equals sign, and then type the code for the special design instruction. See the end of this section for a list of all of these codes. For example, if you want a paragraph to be centered instead of left-aligned, your text would look like this:</p><img data-hederis-type="hblkimg" class="hblkimg" id="pyPyCmbfL" src="/images/pi2.png" data-img-src="pi2.png"/>
    </li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="lisV1PxDwT"><p class="hblkoli" data-hederis-type="hblklip" id="psTVyIoLt">Finally, make sure your cursor is still in the new paragraph, and then open the Styles pane. Scroll to find the HED Processing instruction style name and click on it; this will apply it to your new paragraph.</p></li>
    </ol>
    <p class="hblkp" data-hederis-type="hblkp" id="pCxjEZsZl">You can apply a processing instruction to an entire section by inserting the processing instruction paragraph after the appropriate section start paragraph (see &#8220;<a href="{% post_url 2019-10-21-18-AddaSection %}" id="p3WWFTHKj"><span class="Hyperlink" id="pokgxlRGX">Add a Section</span></a>&#8221;), and to a box by inserting the processing instruction paragraph after either the wrapper start or end paragraph (see &#8220;<a href="{% post_url 2019-10-21-17-AddaWrapper %}" id="p8G3ySyNv"><span class="Hyperlink" id="palRvB5NS">Add a Wrapper</span></a>&#8221;).</p>
    <aside class="hwprbox box" data-hederis-type="hwprbox" id="pNy8PmQwm" data-type="sidebar"><p class="hblktype" data-hederis-type="hblktype" id="pk63DKvry">Tip</p>
    <p class="hblkp" data-hederis-type="hblkp" id="pUFVpAA6T">If you don&#8217;t see the <span class="Emphasis" id="pSu9BXTyB"><em class="hspanem" data-hederis-type="hspanem" id="piApCBC6s">HED Processing instruction</em></span> style in the Styles pane, try adjusting your Styles view options (see &#8220;<a href="{% post_url 2019-10-21-16-Fine-tuneWordStyles %}" id="p6NhyZKzD"><span class="Hyperlink" id="pA4qDSBKC">Fine-tune Word Styles</span></a>&#8221;).</p>
    </aside>
    <aside class="hwprbox box" data-hederis-type="hwprbox" id="ptoTrN2nX" data-type="sidebar"><p class="hblktype" data-hederis-type="hblktype" id="pHd2VRQfO">Tip</p>
    <p class="hblkp" data-hederis-type="hblkp" id="pXyh0OlYT">You can make sure the style was applied by viewing your document in Draft View and expanding the Style area (see &#8220;<a href="{% post_url 2019-10-21-16-Fine-tuneWordStyles %}" id="pTfdHaxXX"><span class="Hyperlink" id="pdovAxot1">Fine-tune Word Styles</span></a>&#8221;).</p>
    </aside>
    <aside class="hwprbox box" data-hederis-type="hwprbox" id="p0ZZgeQEN" data-type="sidebar"><p class="hblktype" data-hederis-type="hblktype" id="pkFrNrKw7">Tip</p>
    <p class="hblkp" data-hederis-type="hblkp" id="p7gDwP0tc">You can apply multiple types of processing instructions to a single paragraph by separating each option with a &#8220;+&#8221;, like this:</p>
    <img data-hederis-type="hblkimg" class="hblkimg" id="pccrgIu9J" src="/images/pi3.png" data-img-src="pi3.png"/>
    </aside>
    <aside class="hwprbox box" data-hederis-type="hwprbox" id="pww1jWsvQ" data-type="sidebar"><p class="hblktype" data-hederis-type="hblktype" id="pyiFx5G8e">Tip</p>
    <p class="hblkp" data-hederis-type="hblkp" id="pC1dwS66P">Some processing instructions accept extra options that change their behavior. For example, the GLOBAL STYLE and ATTRS processing instructions can both accept the SCOPE-BODY option, which will apply your custom instruction to the entire document, rather than to just a single element or group of elements. See &#8220;<a href="{% post_url 2019-10-21-37-Customizethedesignofanentiregroupofparagraphswrappersorsections %}" id="pfeM79fGT"><span class="Hyperlink" id="pYwYNyBa9">Customize the design of an entire group of paragraphs, wrappers, or sections</span></a>&#8221; and &#8220;<a href="{% post_url 2019-10-21-46-AddcustomHTMLattributes %}" id="pxzK2rA0M"><span class="Hyperlink" id="pgGxAzIpj">Add custom HTML attributes</span></a>&#8221; for more info on how to do this.</p>
    </aside>
    <p class="hblkp" data-hederis-type="hblkp" id="pxRX3AGTM">Processing Instruction codes:</p>
    <table id="pima9dkcs" data-hederis-type="hwprtable" class="hwprtable">
      <tr data-hederis-type="hwprtr" class="hwprtr" id="p25BzQG4M">
        <td data-hederis-type="hwprtd" class="hwprtd" id="pHuY1boRs">
          <p class="hblkp" data-hederis-type="hblkp" id="prLjNoZrY"><strong class="hspanstrong" data-hederis-type="hspanstrong" id="pRgwdqfDD">Code</strong></p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="pkq9cXINe">
          <p class="hblkp" data-hederis-type="hblkp" id="pja0UgAKu"><strong class="hspanstrong" data-hederis-type="hspanstrong" id="pTwlgI36M">Possible values</strong></p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="pY4M9Q5El">
          <p class="hblkp" data-hederis-type="hblkp" id="pD0ltQwgb"><strong class="hspanstrong" data-hederis-type="hspanstrong" id="pTBI7dRKn">Notes</strong></p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="pvsZIbInh">
          <p class="hblkp" data-hederis-type="hblkp" id="pghzVjeFu"><strong class="hspanstrong" data-hederis-type="hspanstrong" id="pIO6t2Hob">Documentation</strong></p>
        </td>
      </tr>
      <tr data-hederis-type="hwprtr" class="hwprtr" id="pJPPVNVoV">
        <td data-hederis-type="hwprtd" class="hwprtd" id="plc6C8BQQ">
          <p class="hblkp" data-hederis-type="hblkp" id="p39xhYQx9">IMAGE-SIZE</p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="pKggkZ9Cj">
          <p class="hblkp" data-hederis-type="hblkp" id="prHCzSy9X">fullbleed</p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="pqAhxRH33">
          <p class="hblkp" data-hederis-type="hblkp" id="pv4M0FBET">In the print file, this will create a fullbleed image that will fill an entire page and bleed area. See Images for more info.</p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="pWA7DY8Hw">
          <p class="hblkp" data-hederis-type="hblkp" id="p7ya2kt9i">See &#8220;<a href="{% post_url 2019-10-21-09-Includefull-pageimagesinthePDF %}" id="pnpNqGRcb"><span class="Hyperlink" id="pYJrkZHYn">Include full-page images in the PDF</span></a>&#8221;</p>
        </td>
      </tr>
      <tr data-hederis-type="hwprtr" class="hwprtr" id="pQyTg2CY2">
        <td data-hederis-type="hwprtd" class="hwprtd" id="pXh7GzNSE">
          <p class="hblkp" data-hederis-type="hblkp" id="p43Ua9qyH">STYLE</p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="puORBRM7N">
          <p class="hblkp" data-hederis-type="hblkp" id="plbQkkqeQ">Any valid CSS property/value combination (<a href="https://developer.mozilla.org/en-US/docs/Web/CSS/Reference" id="pUV2yasmQ"><span class="Hyperlink" id="pEKi3OX9N">see this reference</span></a>)</p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="pdXMzSHeC"/>
        <td data-hederis-type="hwprtd" class="hwprtd" id="pScHduEVu">
          <p class="hblkp" data-hederis-type="hblkp" id="pJ7TD1vw0">See &#8220;<a href="{% post_url 2019-10-21-36-Customizethedesignofspecificparagraphswrappersorsections %}" id="pouXT4u0a"><span class="Hyperlink" id="p0pNsboT8">Customize the design of specific paragraphs, wrappers, or sections</span></a>&#8221;</p>
        </td>
      </tr>
      <tr data-hederis-type="hwprtr" class="hwprtr" id="pnAe1GLYo">
        <td data-hederis-type="hwprtd" class="hwprtd" id="pT8HYejZ4">
          <p class="hblkp" data-hederis-type="hblkp" id="p2TAw7Iiq">FORMAT</p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="pfjdfgGLS">
          <p class="hblkp" data-hederis-type="hblkp" id="purlLmj13">ebook, print</p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="pPvogSmK4">
          <p class="hblkp" data-hederis-type="hblkp" id="pXJf2B5AD">Display a certain paragraph, wrapper, or section only in the ebook or PDF file. Default value is &#8220;both&#8221;.</p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="pCsjBJ8dw">
          <p class="hblkp" data-hederis-type="hblkp" id="ptJwFufuu">See &#8220;<a href="{% post_url 2019-10-21-21-IncludecontentonlyinthePDForEPUB %}" id="pbwytMDlj"><span class="Hyperlink" id="p32R6LNFc">Include content only in the PDF or EPUB</span></a>&#8221;</p>
        </td>
      </tr>
      <tr data-hederis-type="hwprtr" class="hwprtr" id="p67MR8GbC">
        <td data-hederis-type="hwprtd" class="hwprtd" id="pdz8LwuWd">
          <p class="hblkp" data-hederis-type="hblkp" id="pjRUGpW7y">GLOBAL STYLE</p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="pAljp7512">
          <p class="hblkp" data-hederis-type="hblkp" id="pPPqAwDDf">Any valid CSS property/value combination (<a href="https://developer.mozilla.org/en-US/docs/Web/CSS/Reference" id="pNRplAnUO"><span class="Hyperlink" id="pk88dloTX">see this reference</span></a>). Also supports the &#8220;SCOPE-BODY&#8221; option.</p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="pZGKsKmq5">
          <p class="hblkp" data-hederis-type="hblkp" id="pON66tegq">To add custom design formatting to an entire group of elements (for example, to add a border around every extract in the entire book).</p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="p5yMhgSHM">
          <p class="hblkp" data-hederis-type="hblkp" id="p4eb06XMT">See &#8220;<a href="{% post_url 2019-10-21-37-Customizethedesignofanentiregroupofparagraphswrappersorsections %}" id="pj0b5fK9I"><span class="Hyperlink" id="pNm8JelIB">Customize the design of an entire group of paragraphs, wrappers, or sections</span></a>&#8221;</p>
        </td>
      </tr>
      <tr data-hederis-type="hwprtr" class="hwprtr" id="pH7Z0yDEX">
        <td data-hederis-type="hwprtd" class="hwprtd" id="pY0EcnEN7">
          <p class="hblkp" data-hederis-type="hblkp" id="p1oP4v98s">ATTRS</p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="pV7sQAAIC">
          <p class="hblkp" data-hederis-type="hblkp" id="pJJtR7AYw">The name and value of one or more <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes" id="pqd7ps035"><span class="Hyperlink" id="p5EzrHDwU">HTML attributes</span></a>. Multiple attributes should be separated by a semi-colon. Also supports the &#8220;SCOPE-BODY&#8221; option.</p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="p7mGQNyDs">
          <p class="hblkp" data-hederis-type="hblkp" id="pIUKrwUuk">You can use <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes" id="pnXVu8dlm"><span class="Hyperlink" id="peox3G8pX">predefined HTML attributes</span></a>, or make up your own attributes that start with the &#8220;data-&#8221; prefix.</p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="pq6Kg8t8r">
          <p class="hblkp" data-hederis-type="hblkp" id="pFDCKuhgo">See &#8220;<a href="{% post_url 2019-10-21-46-AddcustomHTMLattributes %}" id="pd33uD9Dw"><span class="Hyperlink" id="pHqSWse7B">Add custom HTML attributes</span></a>&#8221;</p>
        </td>
      </tr>
    </table>
    <p class="hblkp" data-hederis-type="hblkp" id="pZvRin1PC">Have a suggestion for other types of instructions you might include? Email us! help@hederis.com</p>
    </section>
    