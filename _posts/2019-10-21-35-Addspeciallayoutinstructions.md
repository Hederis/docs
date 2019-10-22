---
layout: default
title:  "Add special layout instructions"
permalink:  /custom-design/
categories: [Design]
tags: [convert,typeset]
published: true
---

<section data-type="chapter" class="hsecchapter" data-hederis-type="hsecchapter" id="custom-design" data-pi-attrs="id: custom-design; data-tags: convert,typeset;" role="doc-chapter" data-tags="convert,typeset" data-author-name=" " data-book-title=" " title="Add special layout instructions"><h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="pecdGIClB">Add special layout instructions</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="pcaW3TlKy">You can tweak the design and layout of specific paragraphs, sections, or wrappers in your book by adding special instructions to your Word file, called <span class="Emphasis" id="pg5EWAg9R"><em class="hspanem" data-hederis-type="hspanem" id="pq79i2xTd">processing instructions</em></span>. We use processing instructions to convey a variety of different types of instructions: customizing running header content, adding CSS styles, adding attributes to the HTML, fixing image sizes, and more.</p>
    <p class="hblkp" data-hederis-type="hblkp" id="pD1DS17Ig">After you&#8217;ve converted your manuscript for the first time, you&#8217;ll receive a new Word file with all of the special Hederis styles applied. (See &#8220;<a href="{% post_url 2019-10-21-16-Fine-tuneWordStyles %}" id="pdCejc2Yi"><span class="Hyperlink" id="pSATLeLTF">Fine-tune Word Styles</span></a>&#8221; for more information on working with Word styles.) We have an extra style just for adding these design and layout instructions: &#8220;HED Processing instruction&#8221;.</p>
    <img data-hederis-type="hblkimg" class="hblkimg" id="pI3Li5f6C" src="/images/pi1.png" data-img-src="pi1.png"/>
    <p class="hblkp" data-hederis-type="hblkp" id="p4Xt3O8TP">To add your processing instructions:</p>
    <ol class="hwprnumlist" data-hederis-type="hwprnumlist" id="pjJsJdkE0"><li class="hblkoli" data-hederis-type="hblkoli" id="li0SqZnS1q"><p class="hblkoli" data-hederis-type="hblklip" id="prfZMgvHG">Find the paragraph that you want to customize the design of, and insert a new paragraph after it (place your cursor at the end of the paragraph, and then press enter).</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="liApTfElFw"><p class="hblkoli" data-hederis-type="hblklip" id="pA21EWFyk">In your new paragraph, type the code for the type of instruction you&#8217;re adding, and then type an equals sign, and then type the code for the special design instruction. See the end of this section for a list of all of these codes. For example, if you want a paragraph to be centered instead of left-aligned, your text would look like this:</p><img data-hederis-type="hblkimg" class="hblkimg" id="pwqZ2aqUT" src="/images/pi2.png" data-img-src="pi2.png"/>
    </li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="lia2JypRiv"><p class="hblkoli" data-hederis-type="hblklip" id="pJBGvGfFO">Finally, make sure your cursor is still in the new paragraph, and then open the Styles pane. Scroll to find the HED Processing instruction style name and click on it; this will apply it to your new paragraph.</p></li>
    </ol>
    <p class="hblkp" data-hederis-type="hblkp" id="pJJz9bfBV">You can apply a processing instruction to an entire section by inserting the processing instruction paragraph after the appropriate section start paragraph (see &#8220;<a href="{% post_url 2019-10-21-18-AddaSection %}" id="pL06El1nW"><span class="Hyperlink" id="pnqOYI3gW">Add a Section</span></a>&#8221;), and to a box by inserting the processing instruction paragraph after either the wrapper start or end paragraph (see &#8220;<a href="{% post_url 2019-10-21-17-AddaWrapper %}" id="pvdWysq4U"><span class="Hyperlink" id="pnapiER5Q">Add a Wrapper</span></a>&#8221;).</p>
    <aside class="hwprbox box" data-hederis-type="hwprbox" id="pFLKcYPdb" data-type="sidebar"><p class="hblktype" data-hederis-type="hblktype" id="pmiGe3Hhk">Tip</p>
    <p class="hblkp" data-hederis-type="hblkp" id="pYCtiCf28">If you don&#8217;t see the <span class="Emphasis" id="ppoh8sdOH"><em class="hspanem" data-hederis-type="hspanem" id="pI4eFREUt">HED Processing instruction</em></span> style in the Styles pane, try adjusting your Styles view options (see &#8220;<a href="{% post_url 2019-10-21-16-Fine-tuneWordStyles %}" id="p9TLDcOgd"><span class="Hyperlink" id="pynY44cyT">Fine-tune Word Styles</span></a>&#8221;).</p>
    </aside>
    <aside class="hwprbox box" data-hederis-type="hwprbox" id="pk1nnoECt" data-type="sidebar"><p class="hblktype" data-hederis-type="hblktype" id="pRpqC59xp">Tip</p>
    <p class="hblkp" data-hederis-type="hblkp" id="pp5ao1MWx">You can make sure the style was applied by viewing your document in Draft View and expanding the Style area (see &#8220;<a href="{% post_url 2019-10-21-16-Fine-tuneWordStyles %}" id="ppISKMfMT"><span class="Hyperlink" id="pxEUZGkSJ">Fine-tune Word Styles</span></a>&#8221;).</p>
    </aside>
    <aside class="hwprbox box" data-hederis-type="hwprbox" id="pzPfODA5d" data-type="sidebar"><p class="hblktype" data-hederis-type="hblktype" id="p2BkJx7Ro">Tip</p>
    <p class="hblkp" data-hederis-type="hblkp" id="pgafphFNS">You can apply multiple types of processing instructions to a single paragraph by separating each option with a &#8220;+&#8221;, like this:</p>
    <img data-hederis-type="hblkimg" class="hblkimg" id="pldPGUtN9" src="/images/pi3.png" data-img-src="pi3.png"/>
    </aside>
    <aside class="hwprbox box" data-hederis-type="hwprbox" id="pIQyRAmg5" data-type="sidebar"><p class="hblktype" data-hederis-type="hblktype" id="p7NwDLx5T">Tip</p>
    <p class="hblkp" data-hederis-type="hblkp" id="pzGHXexki">Some processing instructions accept extra options that change their behavior. For example, the GLOBAL STYLE and ATTRS processing instructions can both accept the SCOPE-BODY option, which will apply your custom instruction to the entire document, rather than to just a single element or group of elements. See &#8220;<a href="{% post_url 2019-10-21-37-Customizethedesignofanentiregroupofparagraphswrappersorsections %}" id="pvk9wpl5H"><span class="Hyperlink" id="ptXDRVuKd">Customize the design of an entire group of paragraphs, wrappers, or sections</span></a>&#8221; and &#8220;<a href="{% post_url 2019-10-21-46-AddcustomHTMLattributes %}" id="pIODP5PDw"><span class="Hyperlink" id="pkOwFb5xa">Add custom HTML attributes</span></a>&#8221; for more info on how to do this.</p>
    </aside>
    <p class="hblkp" data-hederis-type="hblkp" id="p9S36D7wG">Processing Instruction codes:</p>
    <table id="pfMExhVvI" data-hederis-type="hwprtable" class="hwprtable">
      <tr data-hederis-type="hwprtr" class="hwprtr" id="pPQLJhncy">
        <td data-hederis-type="hwprtd" class="hwprtd" id="pcLfCvNvF">
          <p class="hblkp" data-hederis-type="hblkp" id="p5VPQuW1R"><strong class="hspanstrong" data-hederis-type="hspanstrong" id="px35m7KDv">Code</strong></p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="pyYnUmkeT">
          <p class="hblkp" data-hederis-type="hblkp" id="pAqvl63tK"><strong class="hspanstrong" data-hederis-type="hspanstrong" id="pzMEDnYbj">Possible values</strong></p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="pMokh0OqK">
          <p class="hblkp" data-hederis-type="hblkp" id="p6p6jBghk"><strong class="hspanstrong" data-hederis-type="hspanstrong" id="phWIHpDdv">Notes</strong></p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="p2EGd4DTs">
          <p class="hblkp" data-hederis-type="hblkp" id="phl0w4Ekr"><strong class="hspanstrong" data-hederis-type="hspanstrong" id="pJk4SKZAh">Documentation</strong></p>
        </td>
      </tr>
      <tr data-hederis-type="hwprtr" class="hwprtr" id="pnqqix4xt">
        <td data-hederis-type="hwprtd" class="hwprtd" id="plMZvrNeW">
          <p class="hblkp" data-hederis-type="hblkp" id="pBlQTmx3q">IMAGE-SIZE</p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="pKdXCfvEY">
          <p class="hblkp" data-hederis-type="hblkp" id="pGiLRenOU">fullbleed</p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="pzNmbrxL9">
          <p class="hblkp" data-hederis-type="hblkp" id="pHKIFXEVy">In the print file, this will create a fullbleed image that will fill an entire page and bleed area. See Images for more info.</p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="pbtNgWnEq">
          <p class="hblkp" data-hederis-type="hblkp" id="pTZc1ksj1">See &#8220;<a href="{% post_url 2019-10-21-09-Includefull-pageimagesinthePDF %}" id="pH2A646s5"><span class="Hyperlink" id="pE7GEXsAO">Include full-page images in the PDF</span></a>&#8221;</p>
        </td>
      </tr>
      <tr data-hederis-type="hwprtr" class="hwprtr" id="pgYaaPlJQ">
        <td data-hederis-type="hwprtd" class="hwprtd" id="pMNofqMzs">
          <p class="hblkp" data-hederis-type="hblkp" id="p0Fe2woPP">STYLE</p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="pyMZfLwym">
          <p class="hblkp" data-hederis-type="hblkp" id="pWl9pR5tp">Any valid CSS property/value combination (<a href="https://developer.mozilla.org/en-US/docs/Web/CSS/Reference" id="puCpi4RQZ"><span class="Hyperlink" id="pj8sfbu1O">see this reference</span></a>)</p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="pgVnyeRN8"/>
        <td data-hederis-type="hwprtd" class="hwprtd" id="p1XVrw6Mb">
          <p class="hblkp" data-hederis-type="hblkp" id="pRZn0QGBe">See &#8220;<a href="{% post_url 2019-10-21-36-Customizethedesignofspecificparagraphswrappersorsections %}" id="pF5nIw1nU"><span class="Hyperlink" id="pv0DnThC3">Customize the design of specific paragraphs, wrappers, or sections</span></a>&#8221;</p>
        </td>
      </tr>
      <tr data-hederis-type="hwprtr" class="hwprtr" id="pFOWaHk3M">
        <td data-hederis-type="hwprtd" class="hwprtd" id="pFlgxtpjU">
          <p class="hblkp" data-hederis-type="hblkp" id="pm7gtz2Rn">FORMAT</p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="piEjmQiaK">
          <p class="hblkp" data-hederis-type="hblkp" id="pTc6DhM88">ebook, print</p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="pa6SEyoWG">
          <p class="hblkp" data-hederis-type="hblkp" id="pStDQuegS">Display a certain paragraph, wrapper, or section only in the ebook or PDF file. Default value is &#8220;both&#8221;.</p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="p48Q6IfCT">
          <p class="hblkp" data-hederis-type="hblkp" id="pB3nWDs8h">See &#8220;<a href="{% post_url 2019-10-21-21-IncludecontentonlyinthePDForEPUB %}" id="pE2PmJSmg"><span class="Hyperlink" id="p5Daf5V4Y">Include content only in the PDF or EPUB</span></a>&#8221;</p>
        </td>
      </tr>
      <tr data-hederis-type="hwprtr" class="hwprtr" id="pLldkXR8G">
        <td data-hederis-type="hwprtd" class="hwprtd" id="pc4NP02Bq">
          <p class="hblkp" data-hederis-type="hblkp" id="pVJ5R43sI">GLOBAL STYLE</p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="p3tdEj7sH">
          <p class="hblkp" data-hederis-type="hblkp" id="pz93Ek8PU">Any valid CSS property/value combination (<a href="https://developer.mozilla.org/en-US/docs/Web/CSS/Reference" id="pg1y53by2"><span class="Hyperlink" id="pa4zrQ9PW">see this reference</span></a>). Also supports the &#8220;SCOPE-BODY&#8221; option.</p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="p9JiwozoA">
          <p class="hblkp" data-hederis-type="hblkp" id="pZh2npcLq">To add custom design formatting to an entire group of elements (for example, to add a border around every extract in the entire book).</p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="p5PVF4F7R">
          <p class="hblkp" data-hederis-type="hblkp" id="pfgxOsc96">See &#8220;<a href="{% post_url 2019-10-21-37-Customizethedesignofanentiregroupofparagraphswrappersorsections %}" id="pMuhAlhmT"><span class="Hyperlink" id="pMyquFllY">Customize the design of an entire group of paragraphs, wrappers, or sections</span></a>&#8221;</p>
        </td>
      </tr>
      <tr data-hederis-type="hwprtr" class="hwprtr" id="pLQlqQ8E0">
        <td data-hederis-type="hwprtd" class="hwprtd" id="pJ5GBMvw8">
          <p class="hblkp" data-hederis-type="hblkp" id="pfxZ7Du4O">ATTRS</p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="pw94A7mMO">
          <p class="hblkp" data-hederis-type="hblkp" id="pBgMkHi3T">The name and value of one or more <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes" id="pJuTzvyFf"><span class="Hyperlink" id="p7VWhvDuu">HTML attributes</span></a>. Multiple attributes should be separated by a semi-colon. Also supports the &#8220;SCOPE-BODY&#8221; option.</p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="ppYG8DlV0">
          <p class="hblkp" data-hederis-type="hblkp" id="p7P2yFQZ2">You can use <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes" id="ppB9UPFBO"><span class="Hyperlink" id="pWPw65vlM">predefined HTML attributes</span></a>, or make up your own attributes that start with the &#8220;data-&#8221; prefix.</p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="p6CFXCTMa">
          <p class="hblkp" data-hederis-type="hblkp" id="pxSt2WR0Z">See &#8220;<a href="{% post_url 2019-10-21-46-AddcustomHTMLattributes %}" id="p9MYUEzfW"><span class="Hyperlink" id="pOGLThM4o">Add custom HTML attributes</span></a>&#8221;</p>
        </td>
      </tr>
    </table>
    <p class="hblkp" data-hederis-type="hblkp" id="pMHIr7NRt">Have a suggestion for other types of instructions you might include? Email us! help@hederis.com</p>
    </section>
    