# wikiextractor
This is a script that parses a Wikipedia dump and produces plaintext stripping templates, formatting and most of the usual issues in the code.
The original code is from [attardi@github](https://github.com/attardi/wikiextractor), ported by [others](https://github.com/infolab-csail/wikiextractor) to Python3 and here slightly adapted for my specific use case.

The code is old and weird but does its work better than any other tool I know (wkparserfromhell is nice but requires much work to skip elements I don't want) so __use this code only if you have exactly my use case__ (producing a single text file from the compressed dump using Python 3).

## Usage

The only supported usage is this:

    export PYTHONPATH=wikiextractor
    python3 wikiextractor/scripts/WikiExtractor.py --no-template -o - --escapedoc itwiki-20191120-pages-articles.xml.bz2 > dump.txt

The `dump.txt` file will contain the text plus a sort of tag reporting the original title, for example:

    <doc id="2" url="?curid=2" title="Organo a pompa">
    Organo a pompa

    L'organo a pompa è un tipo di [...the whole article in plain text...]

    </doc>
    <doc id="3" url="?curid=3" title="Antropologia">
    ...
