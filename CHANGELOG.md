# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

The major and minor version numbers reflect changes to the DeepL API 
(backward-incompatible and backward-compatible, respectively). The patch version
number is used only for corrections to the OpenAPI specification, for example:
typos, schema fixes, or adding examples.


## [2.15.0] - 2024-07-03
### Added
* Add supported glossary language: Romanian (`ro`).


## [2.14.1] - 2024-06-18
### Changed
* Text translation `context` parameter is now generally available (was alpha).


## [2.14.0] - 2024-05-08
### Added
* Added supported glossary languages: Danish (`'da'`), Norwegian (bokmål) (`'nb'`), and Swedish (`'sv'`).


## [2.13.0] - 2024-03-14
### Deprecated
* Remove all properties from `/usage` except for `character_count` and `character_limit`; 
  these are the only two properties included in the API response for the v2 API. 
### Fixed
* Fixed some minor issues in specs that were violating OpenAPI specification.
  * Thanks to [hoemoon](https://github.com/hoemoon) in [#8](https://github.com/DeepLcom/openapi/pull/8).


## [2.12.0] - 2024-02-29
### Added
* Add supported glossary language: Korean (KO).
* Add supported language for text translation: Arabic (AR). Arabic is 
  currently supported only for text translation; document translation
  support for Arabic is coming soon.


## [2.11.0] - 2023-08-03
### Added
* Add supported glossary languages: Portuguese (PT), Russian (RU), and Chinese (ZH).


## [2.10.0] - 2023-07-13
### Added
* Add JSON-format request bodies to all endpoints except document upload. 


## [2.9.2] - 2023-06-20
### Added
* Japanese (JA) now supports formality.


## [2.9.1] - 2023-05-26
### Fixed
* Fix typo in `/glossaries/{glossary_id}` example and spec version number.
  * Thanks to [cluttrdev](https://github.com/cluttrdev) for the suggestion
    in [#2](https://github.com/DeepLcom/openapi/issues/2).
* Move `description` parameter outside of `allOf` parameter.
  * Thanks to [mikakruschel](https://github.com/mikakruschel) for the suggestion
    in [#1](https://github.com/DeepLcom/openapi/issues/1).


## [2.9.0]
### Added
* Transitive glossaries are now supported, bringing the number of supported
  glossary pairs from 8 to 28.
### Changed 
* Supported XLIFF version 2.1 is now explicitly stated.


## [2.8.0]
### Added
* Add Korean and Norwegian (Bokmål) languages.


## [2.7.0]
### Added
* Add XLIFF to supported document types.


## [2.6.0]
### Changed
* HTML handling is no longer in Beta.
* Removed limit on text parameters (was 50).


## [2.5.0]
### Added
* Add support for EN (English) ←→ NL (Dutch) glossaries.


## [2.4.0]
### Added
* Add formality options prefer_less and prefer_more.
* Add note to readme about Swagger UI simulator and CORS restrictions.


## [2.3.1]
### Fixed
* Source and target language were mixed up in glossary example.
* Fix createGlossary example: remove punctuation. 


## [2.3.0]
### Added
* Add Ukrainian source and target languages.
### Changed
* Add request body size limit to translateText description. 
### Fixed
* Add "Simplified" label to ZH (Chinese) target language.
* Fix a typo in an example.
* Markdown fixes.


## [2.2.0]
### Added
* Add support for EN (English) ←→ PL (Polish) glossaries.
### Fixed
* EN (English) ←→ IT (Italian) was missing from the list of supported glossary
  language pairs in the JSON OpenAPI spec. 


## [2.1.0]
### Added
* Add CSV entries format for creating glossaries.
### Changed
* Rename some tags, reword some descriptions and label default values in
  descriptions.
* Add note about glossaries being immutable, and a workaround for modifying
  glossaries.


## [2.0.0]
Initial release of the OpenAPI specification.


[2.15.0]: https://github.com/DeepLcom/openapi/compare/v2.14.1...v2.15.0
[2.14.1]: https://github.com/DeepLcom/openapi/compare/v2.14.0...v2.14.1
[2.14.0]: https://github.com/DeepLcom/openapi/compare/v2.13.0...v2.14.0
[2.13.0]: https://github.com/DeepLcom/openapi/compare/v2.12.0...v2.13.0
[2.12.0]: https://github.com/DeepLcom/openapi/compare/v2.11.0...v2.12.0
[2.11.0]: https://github.com/DeepLcom/openapi/compare/v2.10.0...v2.11.0
[2.10.0]: https://github.com/DeepLcom/openapi/compare/v2.9.2...v2.10.0
[2.9.2]: https://github.com/DeepLcom/openapi/compare/v2.9.1...v2.9.2
[2.9.1]: https://github.com/DeepLcom/openapi/compare/v2.9.0...v2.9.1
[2.9.0]: https://github.com/DeepLcom/openapi/compare/v2.8.0...v2.9.0
[2.8.0]: https://github.com/DeepLcom/openapi/compare/v2.7.0...v2.8.0
[2.7.0]: https://github.com/DeepLcom/openapi/compare/v2.6.0...v2.7.0
[2.6.0]: https://github.com/DeepLcom/openapi/compare/v2.5.0...v2.6.0
[2.5.0]: https://github.com/DeepLcom/openapi/compare/v2.4.0...v2.5.0
[2.4.0]: https://github.com/DeepLcom/openapi/compare/v2.3.1...v2.4.0
[2.3.1]: https://github.com/DeepLcom/openapi/compare/v2.3.0...v2.3.1
[2.3.0]: https://github.com/DeepLcom/openapi/compare/v2.2.0...v2.3.0
[2.2.0]: https://github.com/DeepLcom/openapi/compare/v2.1.0...v2.2.0
[2.1.0]: https://github.com/DeepLcom/openapi/compare/v2.0.0...v2.1.0
[2.0.0]: https://github.com/DeepLcom/openapi/releases/tag/v2.0.0
