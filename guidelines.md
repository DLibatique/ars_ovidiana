# Guidelines for the Ovidian Focalization Project

These guidelines are a set of instructions for what and how to tag.

`>` indicates that an element (on the left) can include an attribute (on the right) with values specified within each description.

<hr>

## Root element: `book`
* Each book of Ovid's *Metamorphoses* will occupy one XML file.

#### `book` > `n`
* Let `n` = the book number.

<hr>

## Children of `book`:

<hr>

### 1. Word or punctuation token: `token`
* Every word and punctuation mark is its own token.
* Token information generated using the Latin Word Tokenizer function of `cltk`.

#### `token` > `tok-pos`
* the position of the token within its line (bounded by `lb` empty elements).

#### `token` > `postag`
* the part of speech parsing of the token in question, including punctuation from Penn's tags. See POSTag table at end of this documentation.
* postags automatically generated using the Latin 123 NGram Backoff Tagger fuction of `cltk`.

#### `token` > `cite`
* the CTS URN of the given token.

#### `token` > `type`
* if the token is a word of speech or vision, let `type` = "speech" OR "vision" respectively.
* `type` is optional; if the token indicates neither speech nor vision, leave `type` out.

<hr>

### 2. Line beginning: `lb`
* Every line beginning of the book should be marked by an empty `lb` element.

#### `lb` > `n`
* Let `n` = the line number of the tokens that follow.

<hr>

### 3. Direct speech: `said`
* Each instance of direct speech, defined as the span from and including opening quotation marks (' or ") to and including closing quotation marks (again ' or "), should be wrapped in a `said` tag.
* If the direct speech begins at line start, the opening `said` tag should be placed immediately before the `lb` element.
* If the direct speech ends at line end, the closing `said` tag should be placed immediately before the next `lb` element.

Example:

```
<!-- Note the position of the opening said tag, before the following `lb` element. -->
<said degree="2" speaker="Jupiter" cite="urn:cts:latinLit:phi0959.phi006:1.209-1.243">

<lb n="209"/>
<token tok-pos="1" postag='"' cite="urn:cts:latinLit:phi0959.phi006:1.209">"</token>
<token tok-pos="2" postag="PD-S---MN-" cite="urn:cts:latinLit:phi0959.phi006:1.209">Ille</token>
<token tok-pos="3" postag="D---------" cite="urn:cts:latinLit:phi0959.phi006:1.209">quidem</token>

...

<token tok-pos="9" postag="N--P---FA-" cite="urn:cts:latinLit:phi0959.phi006:1.243">poenas</token>
<token tok-pos="10" postag="." cite="urn:cts:latinLit:phi0959.phi006:1.243">.</token>
<token tok-pos="11" postag='"' cite="urn:cts:latinLit:phi0959.phi006:1.243">"</token>

<!-- Note the position of the closing said tag, between the closing quotation mark token and the following `lb` tag. -->
</said>

<lb n="244"/>
<token tok-pos="1" postag="N--P---NA-" cite="urn:cts:latinLit:phi0959.phi006:1.244" type="speech">Dicta</token>

...
```

#### `said` > `degree`
* `degree` indicates the level of narration that the speaker occupies.
    * The omniscient narrator of the *Metamorphoses* always occupies degree 1.
    * A character speaking in direct speech will occupy degree 2.
    * A character whose speech is reported by a degree 2 character will occupy degree 3.
    * These levels of narration can continue indefinitely.

#### `said` > `speaker`
* `speaker` indicates the character(s) speaking the direct speech wrapped by the `said` tag.

#### `said` > `cite`
* `cite` gives the entire CTS URN for the block of direct speech, from opening quotation mark to closing quotation mark.
* The `cite` attribute of `said` is concerned only with the immediate context of the direct speech in question.
    * So, if the direct speech in question is spoken by a character at the third degree (`degree='3'`), `cite` will indicate the citation for *that* character's speech, not the citation for the speech that *contains* the third degree character's speech.
