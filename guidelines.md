# Guidelines for the ARS Ovidiana Project

These guidelines are a set of instructions for what and how to tag.

`>` indicates that an element (on the left) can include an attribute (on the right) with values specified within each description.

<hr>

## Root element: `book`
* Each book of Ovid's *Metamorphoses* will occupy one XML file.

#### `book` > `n`
* `n` = the book number.

<hr>

## Children of `book`:

<hr>

### 1. Word or punctuation token: `token`
* Every word and punctuation mark is its own token.
* Token information generated using the Latin Word Tokenizer function of `cltk`.

#### `token` > `tok-pos`
* the position of the token within its line (bounded by `lb` empty elements).

#### `token` > `cite`
* the CTS URN of the given token.

#### `token` > `type`
* if the token is a word of speech or vision, let `type` = "speech" OR "vision" respectively.
* `type` is optional; if the token indicates neither speech nor vision, leave `type` out.
* "speech" and "vision" can be defined broadly.
    * "speech" can indicate anything from voice and speaking to asking, singing, commanding; any word entity that includes a communicative aspect in its denotation.
    * "speech" can also tag its natural opposites, e.g., muteness, silence, etc.
    * "vision" can indicate anything from eyes and seeing to images, physical perception, reading; any word entity that includes a visual element in its denotation.
    * "vision" can also tag its natural opposites, e.g., blindness.

#### `token` > `postag`
* the part of speech parsing of the token in question, including punctuation from Penn's tags.
* postags automatically generated using the Latin 123 NGram Backoff Tagger fuction of `cltk`. They all need to be vetted by hand.

*  `postag` key:

Every POS tag, except for punctuation tags, should have 10 slots. If a category does not apply to the token in question, use a single hyphen (-) as a placeholder in that category.

Each item of the category should be either a hyphen (-) or an *uppercase* letter.

These definitions are drawn from Logeion / Perseus at Chicago.

##### 1: major part of speech
* **V**erb,
* **N**oun,
* **A**djective,
* **P**ronoun,
* a**D**verb,
* **C**onjunction,
* p**R**eposition,
* particle = **G**,
* p**U**nctuation

##### 2: minor part of speech OR punctuation
* Some tags in this slot can attach only to certain parts of speech. Determine the tag in slot 1 (major part of speech) based on the description of the tag. e.g., a possessive pronoun's first two slots will read PS. A demonstrative adjective's first two slots will read AD.
* Minor part of speech:
    * **S**: possessive pronoun,
    * **M**: modal particle,
    * **A**: determinatives (*is, ipse, idem*),
    * **D**emonstrative (*hic*, *ille*, *ipse*)
    * **I**nterrogative (*quis*, *quid*),
    * **R**elative (*qui*),
    * po**S**sessive,
    * **X**: indefinite,
    * **P**ersonal  
* Punctuation:
    * **Q**uotation mark
    * **L**eft parenthesis [ ( { <
    * ri**G**ht parenthesis ] ) } >
    * **C**omma ,
    * Sentence-**F**inal punctuation . ! ?
    * Sentence-Middl**E** punctuation : ; ... -- -

##### 3: Person
* 1, 2, or 3

##### 4: Number
* **S**ingular or **P**lural

##### 5: Tense
* **P**resent, **I**mperfect, pe**R**fect, **F**uture, p**L**uperfect, fu**T**ure perfect

##### 6: Mood
* **I**ndicative, **S**ubjunctive, i**M**perative, **P**articiple, i**N**finitive, **G**erundive, gerun**D**, s**U**pine

##### 7: Voice
* **A**ctive or **P**assive

##### 8: Gender
* **M**asculine, **F**eminine, **N**euter

##### 9: Case
* **N**ominative, **G**enitive, **D**ative, **A**ccusative, a**B**lative, **V**ocative

##### 10: Degree
* **P**ositive, **C**omparative, **S**uperlative

##### Punctuation
* If the POS tag is for punctuation, you should use a single item, listed as follows, and leave out the remaining 9 slots.
* " = quotation mark ' or "
* ( = left parenthesis [, (, {, <
* ) = right parenthesis ], ), }, >
* , = comma
* . = sentence-final punctuation . ! ?
* : = mid-sentence punctuation : ; ... -- -

##### Examples

> puella, in illa arbore sedens, puerum vocat ut eum videat.

word | postag
--- | ---
puella | `N--S---FN-`
, | `,`
in | `R---------`
illa | `PD-S---FB-`
arbore | `N--S---FB-`
sedens | `V--PPAFN-`
, | `,`
puerum | `N--S---MA-`
vocat | `V-3SPIA---`
ut | `C---------`
eum | `PA-S---MA-`
videat | `V-3SPSA---`

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
    * First-person references and second-person addresses by the omniscient narrator should be tagged as degree="1" with speaker="Narrator" (see next section).

#### `said` > `speaker`
* `speaker` indicates the character(s) speaking the direct speech wrapped by the `said` tag.

#### `said` > `cite`
* `cite` gives the entire CTS URN for the block of direct speech, from opening quotation mark to closing quotation mark.
* The `cite` attribute of `said` is concerned only with the immediate context of the direct speech in question.
    * So, if the direct speech in question is spoken by a character at the third degree (`degree='3'`), `cite` will indicate the citation for *that* character's speech, not the citation for the speech that *contains* the third degree character's speech.
