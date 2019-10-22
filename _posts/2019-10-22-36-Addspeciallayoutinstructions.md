---
layout: default
title:  "Add special layout instructions"
permalink:  /custom-design/
categories: [Design]
tags: [convert,typeset]
published: true
---

<section data-type="chapter" class="hsecchapter" data-hederis-type="hsecchapter" id="custom-design" data-pi-attrs="id: custom-design; data-tags: convert,typeset;" role="doc-chapter" data-tags="convert,typeset" data-author-name=" " data-book-title=" " title="Add special layout instructions"><h1 data-hederis-type="hblkchaptitle" class="hblkchaptitle" id="pPC29lc23">Add special layout instructions</h1>
    <p class="hblkp" data-hederis-type="hblkp" id="pLCj66p7g">You can tweak the design and layout of specific paragraphs, sections, or wrappers in your book by adding special instructions to your Word file, called <span class="Emphasis" id="poY75bw8I"><em class="hspanem" data-hederis-type="hspanem" id="pYvIjVzPo">processing instructions</em></span>. We use processing instructions to convey a variety of different types of instructions: customizing running header content, adding CSS styles, adding attributes to the HTML, fixing image sizes, and more.</p>
    <p class="hblkp" data-hederis-type="hblkp" id="pQeaTOmrg">After you&#8217;ve converted your manuscript for the first time, you&#8217;ll receive a new Word file with all of the special Hederis styles applied. (See &#8220;<a href="{% post_url 2019-10-22-16-Fine-tuneWordStyles %}" id="psbOjcdAu"><span class="Hyperlink" id="pwg2yBAib">Fine-tune Word Styles</span></a>&#8221; for more information on working with Word styles.) We have an extra style just for adding these design and layout instructions: &#8220;HED Processing instruction&#8221;.</p>
    <img data-hederis-type="hblkimg" class="hblkimg" id="peX8Nlxnw" src="/images/pi1.png" data-img-src="pi1.png"/>
    <p class="hblkp" data-hederis-type="hblkp" id="p4lWFUXV1">To add your processing instructions:</p>
    <ol class="hwprnumlist" data-hederis-type="hwprnumlist" id="p0UEsrbp6"><li class="hblkoli" data-hederis-type="hblkoli" id="liJ8HO8bYp"><p class="hblkoli" data-hederis-type="hblklip" id="puKCFdJwi">Find the paragraph that you want to customize the design of, and insert a new paragraph after it (place your cursor at the end of the paragraph, and then press enter).</p></li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="liJPIvX5LV"><p class="hblkoli" data-hederis-type="hblklip" id="pBSmdEbj3">In your new paragraph, type the code for the type of instruction you&#8217;re adding, and then type an equals sign, and then type the code for the special design instruction. See the end of this section for a list of all of these codes. For example, if you want a paragraph to be centered instead of left-aligned, your text would look like this:</p><img data-hederis-type="hblkimg" class="hblkimg" id="pU5hj3RHS" src="/images/pi2.png" data-img-src="pi2.png"/>
    </li>
    <li class="hblkoli" data-hederis-type="hblkoli" id="litnDKZvJt"><p class="hblkoli" data-hederis-type="hblklip" id="pHPGCaeC8">Finally, make sure your cursor is still in the new paragraph, and then open the Styles pane. Scroll to find the HED Processing instruction style name and click on it; this will apply it to your new paragraph.</p></li>
    </ol>
    <p class="hblkp" data-hederis-type="hblkp" id="pGh7ltxQr">You can apply a processing instruction to an entire section by inserting the processing instruction paragraph after the appropriate section start paragraph (see &#8220;<a href="{% post_url 2019-10-22-18-AddaSection %}" id="pQVRC6DtQ"><span class="Hyperlink" id="p6BmqUp2W">Add a Section</span></a>&#8221;), and to a box by inserting the processing instruction paragraph after either the wrapper start or end paragraph (see &#8220;<a href="{% post_url 2019-10-22-17-AddaWrapper %}" id="pgb2GK7Yf"><span class="Hyperlink" id="pJLM0EFJh">Add a Wrapper</span></a>&#8221;).</p>
    <aside class="hwprbox box" data-hederis-type="hwprbox" id="pZB4sQvFW" data-type="sidebar"><p class="hblktype" data-hederis-type="hblktype" id="pLWqrXz1S">Tip</p>
    <p class="hblkp" data-hederis-type="hblkp" id="pNqbCYRLw">If you don&#8217;t see the <span class="Emphasis" id="pt8PztNjy"><em class="hspanem" data-hederis-type="hspanem" id="pfSVVOds9">HED Processing instruction</em></span> style in the Styles pane, try adjusting your Styles view options (see &#8220;<a href="{% post_url 2019-10-22-16-Fine-tuneWordStyles %}" id="pkYP3Iuf9"><span class="Hyperlink" id="pJhFhjbV3">Fine-tune Word Styles</span></a>&#8221;).</p>
    </aside>
    <aside class="hwprbox box" data-hederis-type="hwprbox" id="pnzJHp3mY" data-type="sidebar"><p class="hblktype" data-hederis-type="hblktype" id="p1EKpjskQ">Tip</p>
    <p class="hblkp" data-hederis-type="hblkp" id="ppyOz5SNa">You can make sure the style was applied by viewing your document in Draft View and expanding the Style area (see &#8220;<a href="{% post_url 2019-10-22-16-Fine-tuneWordStyles %}" id="pQfn3cAgU"><span class="Hyperlink" id="piMzLvIhD">Fine-tune Word Styles</span></a>&#8221;).</p>
    </aside>
    <aside class="hwprbox box" data-hederis-type="hwprbox" id="pxlwd2oUI" data-type="sidebar"><p class="hblktype" data-hederis-type="hblktype" id="pE7UwgDrL">Tip</p>
    <p class="hblkp" data-hederis-type="hblkp" id="pudfJ8tWP">You can apply multiple types of processing instructions to a single paragraph by separating each option with a &#8220;+&#8221;, like this:</p>
    <img data-hederis-type="hblkimg" class="hblkimg" id="pZETOwyNO" src="/images/pi3.png" data-img-src="pi3.png"/>
    </aside>
    <aside class="hwprbox box" data-hederis-type="hwprbox" id="pEJh0WgbQ" data-type="sidebar"><p class="hblktype" data-hederis-type="hblktype" id="pxK5yI2eN">Tip</p>
    <p class="hblkp" data-hederis-type="hblkp" id="pmXGHROJu">Some processing instructions accept extra options that change their behavior. For example, the GLOBAL STYLE and ATTRS processing instructions can both accept the SCOPE-BODY option, which will apply your custom instruction to the entire document, rather than to just a single element or group of elements. See &#8220;<a href="{% post_url 2019-10-22-38-Customizethedesignofanentiregroupofparagraphswrappersorsections %}" id="pVysXlXdH"><span class="Hyperlink" id="pDTtvu9yj">Customize the design of an entire group of paragraphs, wrappers, or sections</span></a>&#8221; and &#8220;<a href="{% post_url 2019-10-22-47-AddcustomHTMLattributes %}" id="pYjMkgoej"><span class="Hyperlink" id="pZiYd03fm">Add custom HTML attributes</span></a>&#8221; for more info on how to do this.</p>
    </aside>
    <p class="hblkp" data-hederis-type="hblkp" id="pUnWKaR6R">Processing Instruction codes:</p>
    <table id="puz30mnIG" data-hederis-type="hwprtable" class="hwprtable">
      <tr data-hederis-type="hwprtr" class="hwprtr" id="pfXmhMKIU">
        <td data-hederis-type="hwprtd" class="hwprtd" id="p9FEqnjOh">
          <p class="hblkp" data-hederis-type="hblkp" id="pTuyKIkSG"><strong class="hspanstrong" data-hederis-type="hspanstrong" id="pzFJq6Iyz">Code</strong></p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="pFyKJXgrJ">
          <p class="hblkp" data-hederis-type="hblkp" id="pQ8YCRGqs"><strong class="hspanstrong" data-hederis-type="hspanstrong" id="pCqsoWcLY">Possible values</strong></p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="prYgxlXwY">
          <p class="hblkp" data-hederis-type="hblkp" id="pDkvItqlj"><strong class="hspanstrong" data-hederis-type="hspanstrong" id="pxd0O2FtA">Notes</strong></p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="pxEYZhSpu">
          <p class="hblkp" data-hederis-type="hblkp" id="pXYSDXG5P"><strong class="hspanstrong" data-hederis-type="hspanstrong" id="pvkFIWtXR">Documentation</strong></p>
        </td>
      </tr>
      <tr data-hederis-type="hwprtr" class="hwprtr" id="pipZIbnKr">
        <td data-hederis-type="hwprtd" class="hwprtd" id="pNtKWlbk0">
          <p class="hblkp" data-hederis-type="hblkp" id="pcukplfJE">IMAGE-SIZE</p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="pfOMCdpQK">
          <p class="hblkp" data-hederis-type="hblkp" id="pUooY2g0l">fullbleed</p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="pT8L7Qyfj">
          <p class="hblkp" data-hederis-type="hblkp" id="pBB7twWzN">In the print file, this will create a fullbleed image that will fill an entire page and bleed area. See Images for more info.</p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="pW4jpyYmr">
          <p class="hblkp" data-hederis-type="hblkp" id="pols44AU6">See &#8220;<a href="{% post_url 2019-10-22-09-Includefull-pageimagesinthePDF %}" id="pxnoEq70n"><span class="Hyperlink" id="pUUkcV3Kd">Include full-page images in the PDF</span></a>&#8221;</p>
        </td>
      </tr>
      <tr data-hederis-type="hwprtr" class="hwprtr" id="pzikjvIay">
        <td data-hederis-type="hwprtd" class="hwprtd" id="pKLZerWMU">
          <p class="hblkp" data-hederis-type="hblkp" id="prLqGJuJ1">STYLE</p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="pRe8xcapF">
          <p class="hblkp" data-hederis-type="hblkp" id="pxrzIMLAb">Any valid CSS property/value combination (<a href="https://developer.mozilla.org/en-US/docs/Web/CSS/Reference" id="ppPggkc0b"><span class="Hyperlink" id="p6Pa2IlwW">see this reference</span></a>)</p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="pgE6TyuZp"/>
        <td data-hederis-type="hwprtd" class="hwprtd" id="pku7pr0Sq">
          <p class="hblkp" data-hederis-type="hblkp" id="pKuSkWYBC">See &#8220;<a href="{% post_url 2019-10-22-37-Customizethedesignofspecificparagraphswrappersorsections %}" id="pHYZtPkAq"><span class="Hyperlink" id="pB5dYzguf">Customize the design of specific paragraphs, wrappers, or sections</span></a>&#8221;</p>
        </td>
      </tr>
      <tr data-hederis-type="hwprtr" class="hwprtr" id="p8zBMD2RA">
        <td data-hederis-type="hwprtd" class="hwprtd" id="pI1myg8l0">
          <p class="hblkp" data-hederis-type="hblkp" id="pdXcndE1I">FORMAT</p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="psFRmvnsi">
          <p class="hblkp" data-hederis-type="hblkp" id="pYOvjvKMJ">ebook, print</p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="pfYqW2MeJ">
          <p class="hblkp" data-hederis-type="hblkp" id="pevyp0BDY">Display a certain paragraph, wrapper, or section only in the ebook or PDF file. Default value is &#8220;both&#8221;.</p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="pvMZ2Djnc">
          <p class="hblkp" data-hederis-type="hblkp" id="pRoYbF7xf">See &#8220;<a href="{% post_url 2019-10-22-21-IncludecontentonlyinthePDForEPUB %}" id="p15FqDGIg"><span class="Hyperlink" id="pssniSLmd">Include content only in the PDF or EPUB</span></a>&#8221;</p>
        </td>
      </tr>
      <tr data-hederis-type="hwprtr" class="hwprtr" id="p8391rO1i">
        <td data-hederis-type="hwprtd" class="hwprtd" id="pXCFkW3Cs">
          <p class="hblkp" data-hederis-type="hblkp" id="pIgqBjcHh">GLOBAL STYLE</p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="pkNBzR99F">
          <p class="hblkp" data-hederis-type="hblkp" id="p3ZMf1hXW">Any valid CSS property/value combination (<a href="https://developer.mozilla.org/en-US/docs/Web/CSS/Reference" id="pyoHWf23G"><span class="Hyperlink" id="p4DX68C8T">see this reference</span></a>). Also supports the &#8220;SCOPE-BODY&#8221; option.</p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="pnO6YWN59">
          <p class="hblkp" data-hederis-type="hblkp" id="pF1GPWNWi">To add custom design formatting to an entire group of elements (for example, to add a border around every extract in the entire book).</p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="p85QRj2AE">
          <p class="hblkp" data-hederis-type="hblkp" id="pbgLnANk9">See &#8220;<a href="{% post_url 2019-10-22-38-Customizethedesignofanentiregroupofparagraphswrappersorsections %}" id="pDPRv0UVN"><span class="Hyperlink" id="p6iv7pH16">Customize the design of an entire group of paragraphs, wrappers, or sections</span></a>&#8221;</p>
        </td>
      </tr>
      <tr data-hederis-type="hwprtr" class="hwprtr" id="poy68uFdv">
        <td data-hederis-type="hwprtd" class="hwprtd" id="pWQj9Q1eK">
          <p class="hblkp" data-hederis-type="hblkp" id="pGBPLXM2E">ATTRS</p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="pPc1a3YTb">
          <p class="hblkp" data-hederis-type="hblkp" id="p0uL40IwI">The name and value of one or more <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes" id="pSoMm0o1j"><span class="Hyperlink" id="p6AGVyg3G">HTML attributes</span></a>. Multiple attributes should be separated by a semi-colon. Also supports the &#8220;SCOPE-BODY&#8221; option.</p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="pli2VjBFD">
          <p class="hblkp" data-hederis-type="hblkp" id="pIgjMTsHX">You can use <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes" id="pSh5pu4CF"><span class="Hyperlink" id="pzFvSOOzz">predefined HTML attributes</span></a>, or make up your own attributes that start with the &#8220;data-&#8221; prefix.</p>
        </td>
        <td data-hederis-type="hwprtd" class="hwprtd" id="pknBXKQtv">
          <p class="hblkp" data-hederis-type="hblkp" id="pz4upRijI">See &#8220;<a href="{% post_url 2019-10-22-47-AddcustomHTMLattributes %}" id="pzbEwyR4v"><span class="Hyperlink" id="pHkU5fhJ1">Add custom HTML attributes</span></a>&#8221;</p>
        </td>
      </tr>
    </table>
    <p class="hblkp" data-hederis-type="hblkp" id="pbbLjRIw4">Have a suggestion for other types of instructions you might include? Email us! help@hederis.com</p>
    </section>
    