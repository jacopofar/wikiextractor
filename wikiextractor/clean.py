from wikiextractor.extract import Extractor, ignoreTag, resetIgnoredTags


def clean_markup(markup, accepted_namespaces, keep_links=False, ignore_headers=True):
    """
    Clean Wikimarkup to produce plaintext.

    :param keep_links: Set to True to keep internal and external links
    :param ignore_headers: if set to True, the output list will not contain
    headers, only

    Returns a list of paragraphs (unicode strings).
    """

    if not keep_links:
        ignoreTag('a')
    extractor = Extractor(0, '', [])

    # returns a list of strings
    paragraphs = extractor.clean_text(markup,
                                      accepted_namespaces,
                                      mark_headers=True,
                                      expand_templates=False,
                                      escape_doc=True)
    resetIgnoredTags()

    if ignore_headers:
        paragraphs = [s for s in paragraphs if not s.startswith('## ')]

    return paragraphs
