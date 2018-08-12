"""
The wos fields definitions.
"""

import collections
import functools


IsiField = collections.namedtuple(
    'IsiField',
    ['key', 'description', 'parse', 'aliases']
)


def joined(seq, sep=' '):
    return sep.join(s.strip() for s in seq)


def ident(seq):
    return list(s.strip() for s in seq)


def delimited(seq, delim='; '):
    return joined(seq).split(delim)


def integer(seq):
    return int(joined(seq).strip())


FIELDS = {
    'AB': IsiField(
        'AB',
        'Abstract',
        joined,
        ['abstract']
    ),
    'AF': IsiField(
        'AF',
        'Author Full Names',
        ident,
        ['author_full_names']
    ),
    'AR': IsiField(
        'AR',
        'Article Number',
        joined,
        ['article_number']
    ),
    'AU': IsiField(
        'AU',
        'Authors',
        ident,
        ['authors']
    ),
    'BA': IsiField(
        'BA',
        'Book Authors',
        ident,
        ['book_authors']
    ),
    'BE': IsiField(
        'BE',
        'Editors',
        ident,
        ['editors']
    ),
    'BF': IsiField(
        'BF',
        'Book Authors Full Name',
        ident,
        ['book_authors_full_name']
    ),
    'BN': IsiField(
        'BN',
        'International Standard Book Number (ISBN)',
        joined,
        ['international_standard_book_number']
    ),
    'BP': IsiField(
        'BP',
        'Beginning Page',
        joined,
        ['beginning_page']
    ),
    'BS': IsiField(
        'BS',
        'Book Series Subtitle',
        joined,
        ['book_series_subtitle']
    ),
    'C1': IsiField(
        'C1',
        'Author Address',
        ident,
        ['author_address']
    ),
    'CA': IsiField(
        'CA',
        'Group Authors',
        ident,
        ['group_authors']
    ),
    'CL': IsiField(
        'CL',
        'Conference Location',
        joined,
        ['conference_location']
    ),
    'CR': IsiField(
        'CR',
        'Cited References',
        ident,
        ['cited_references', 'references', 'citations']
    ),
    'CT': IsiField(
        'CT',
        'Conference Title',
        functools.partial(joined, sep='\n'),
        ['conference_title']
    ),
    'CY': IsiField(
        'CY',
        'Conference Date',
        joined,
        ['conference_date']
    ),
    'DE': IsiField(
        'DE',
        'Author Keywords',
        delimited,
        ['author_keywords']
    ),
    'DI': IsiField(
        'DI',
        'Digital Object Identifier (DOI)',
        joined,
        ['digital_object_identifier']
    ),
    'DT': IsiField(
        'DT',
        'Document Type',
        joined,
        ['document_type']
    ),
    'D2': IsiField(
        'D2',
        'Book Digital Object Identifier (DOI)',
        joined,
        ['book_digital_object_identifier']
    ),
    'ED': IsiField(
        'ED',
        'Editors',
        ident,
        ['editors']
    ),
    'EM': IsiField(
        'EM',
        'E-mail Address',
        ident,
        ['e-mail_address']
    ),
    'EI': IsiField(
        'EI',
        'Electronic International Standard Serial Number (eISSN)',
        joined,
        ['eissn']
    ),
    'EP': IsiField(
        'EP',
        'Ending Page',
        joined,
        ['ending_page']
    ),
    'FU': IsiField(
        'FU',
        'Funding Agency and Grant Number',
        delimited,
        ['funding_agency_and_grant_number']
    ),
    'FX': IsiField(
        'FX',
        'Funding Text',
        joined,
        ['funding_text']
    ),
    'GA': IsiField(
        'GA',
        'Document Delivery Number',
        joined,
        ['document_delivery_number']
    ),
    'GP': IsiField(
        'GP',
        'Book Group Authors',
        ident,
        ['book_group_authors']
    ),
    'HO': IsiField(
        'HO',
        'Conference Host',
        joined,
        ['conference_host']
    ),
    'ID': IsiField(
        'ID',
        'Keywords Plus',
        delimited,
        ['keywords_plus', 'keywords']
    ),
    'IS': IsiField(
        'IS',
        'Issue',
        joined,
        ['issue']
    ),
    'J9': IsiField(
        'J9',
        '29-Character Source Abbreviation',
        joined,
        ['source_abbreviation']
    ),
    'JI': IsiField(
        'JI',
        'ISO Source Abbreviation',
        joined,
        ['iso_source_abbreviation']
    ),
    'LA': IsiField(
        'LA',
        'Language',
        joined,
        ['language']
    ),
    'MA': IsiField(
        'MA',
        'Meeting Abstract',
        joined,
        ['meeting_abstract']
    ),
    'NR': IsiField(
        'NR',
        'Cited Reference Count',
        integer,
        ['cited_reference_count']
    ),
    'OI': IsiField(
        'OI',
        'ORCID Identifier (Open Researcher and Contributor ID)',
        delimited,
        ['orcid_identifier']
    ),
    'P2': IsiField(
        'P2',
        'Chapter count (Book Citation Index)',
        integer,
        ['chapter_count']
    ),
    'PA': IsiField(
        'PA',
        'Publisher Address',
        functools.partial(joined, sep='\n'),
        ['publisher_address']
    ),
    'PD': IsiField(
        'PD',
        'Publication Date',
        joined,
        ['publication_date']
    ),
    'PG': IsiField(
        'PG',
        'Page Count',
        integer,
        ['page_count']
    ),
    'PI': IsiField(
        'PI',
        'Publisher City',
        joined,
        ['publisher_city']
    ),
    'PM': IsiField(
        'PM',
        'PubMed ID',
        joined,
        ['pubmed_id']
    ),
    'PN': IsiField(
        'PN',
        'Part Number',
        joined,
        ['part_number']
    ),
    'PT': IsiField(
        'PT',
        'Publication Type (J=Journal; B=Book; S=Series; P=Patent)',
        joined,
        ['publication_type']
    ),
    'PU': IsiField(
        'PU',
        'Publisher',
        joined,
        ['publisher']
    ),
    'PY': IsiField(
        'PY',
        'Year Published',
        integer,
        ['year_published']
    ),
    'RI': IsiField(
        'RI',
        'ResearcherID Number',
        delimited,
        ['researcherid_number']
    ),
    'RP': IsiField(
        'RP',
        'Reprint Address',
        joined,
        ['reprint_address']
    ),
    'SC': IsiField(
        'SC',
        'Research Areas',
        delimited,
        ['research_areas']
    ),
    'SE': IsiField(
        'SE',
        'Book Series Title',
        joined,
        ['book_series_title']
    ),
    'SI': IsiField(
        'SI',
        'Special Issue',
        joined,
        ['special_issue']
    ),
    'SN': IsiField(
        'SN',
        'International Standard Serial Number (ISSN)',
        joined,
        ['issn']
    ),
    'SO': IsiField(
        'SO',
        'Publication Name',
        joined,
        ['publication_name']
    ),
    'SP': IsiField(
        'SP',
        'Conference Sponsors',
        functools.partial(delimited, delim=', '),
        ['conference_sponsors']
    ),
    'SU': IsiField(
        'SU',
        'Supplement',
        joined,
        ['supplement']
    ),
    'TC': IsiField(
        'TC',
        'Web of Science Core Collection Times Cited Count',
        integer,
        ['wos_times_cited_count', 'wos_times_cited']
    ),
    'TI': IsiField(
        'TI',
        'Document Title',
        joined,
        ['title']
    ),
    'U1': IsiField(
        'U1',
        'Usage Count (Last 180 Days)',
        integer,
        ['usage_count']
    ),
    'U2': IsiField(
        'U2',
        'Usage Count (Since 2013)',
        integer,
        ['usage_count']
    ),
    'UT': IsiField(
        'UT',
        'Unique Article Identifier',
        joined,
        ['unique_article_identifier']
    ),
    'VL': IsiField(
        'VL',
        'Volume',
        joined,
        ['volume']
    ),
    'WC': IsiField(
        'WC',
        'Web of Science Categories',
        delimited,
        ['web_of_science_categories']
    ),
    'Z9': IsiField(
        'Z9',
        'Total Times Cited Count (WoS Core, BCI, and CSCD)',
        integer,
        ['total_times_cited_count', 'times_cited']
    ),
}


def field_aliases():
    for fields in FIELDS.values():
        yield fields.aliases[-1]


def preprocess(raw_dict):
    processed_data = {}
    raw_dict.setdefault('CR', [])
    for key, seq in raw_dict.items():
        if key in FIELDS:
            field = FIELDS[key]
            parsed = field.parse(seq)
            processed_data[key] = parsed
            for alias in field.aliases:
                processed_data[alias] = parsed
        else:
            processed_data[key] = ' '.join(seq)
    return processed_data
