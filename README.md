# DeepL API Specifications

This repository contains [OpenAPI][openapi-specification] and [AsyncAPI][asyncapi-specification] specifications for the [DeepL API][deepl-api], in YAML and JSON formats.

## Public mirror

This is a public mirror of the DeepL API specifications. Specs are synced automatically from [DeepLcom/api-docs](https://github.com/DeepLcom/api-docs):

- [`openapi.yaml`](openapi.yaml) / [`openapi.json`](openapi.json) — DeepL REST API (translate, glossaries, documents, etc.)
- [`voice.asyncapi.yaml`](voice.asyncapi.yaml) / [`voice.asyncapi.json`](voice.asyncapi.json) — DeepL Voice API (audio transcription and translation)

For the most up-to-date specifications, see the source files in [api-docs](https://github.com/DeepLcom/api-docs/tree/main/api-reference).

## Usage

You can use these specifications to explore the API in tools like [Postman][postman], or to auto-generate SDKs and code libraries using tools such as [Swagger Editor][swagger-editor] or [OpenAPI Generator][openapi-generator].

Note that running the request in a browser will fail due to [CORS][cors-docs] restrictions.

[asyncapi-specification]: https://www.asyncapi.com/

[cors-docs]: https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS

[deepl-api]: https://www.deepl.com/pro-api

[openapi-generator]: https://openapi-generator.tech/

[openapi-specification]: https://openapis.org/

[postman]: https://www.postman.com/

[swagger-editor]: https://editor.swagger.io/?url=https://raw.githubusercontent.com/DeepLcom/openapi/main/openapi.yaml
