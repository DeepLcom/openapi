# DeepL API Specifications

This repository contains [OpenAPI][openapi-specification] and [AsyncAPI][asyncapi-specification] specifications for the [DeepL API][deepl-api], in YAML and JSON formats.

## Public mirror

This is a public mirror of the DeepL API specifications. Specs are synced automatically from [DeepLcom/api-docs](https://github.com/DeepLcom/api-docs):

- [`openapi.yaml`](openapi.yaml) / [`openapi.json`](openapi.json) — DeepL REST API (translate, glossaries, documents, etc.)
- [`voice.asyncapi.yaml`](voice.asyncapi.yaml) / [`voice.asyncapi.json`](voice.asyncapi.json) — DeepL Voice API (WebSocket streaming)

For the most up-to-date specifications, see the source files in [api-docs](https://github.com/DeepLcom/api-docs/tree/main/api-reference).

## Usage

You can use these specifications to explore the API in tools like [Postman][postman], or to auto-generate SDKs and code libraries using tools such as [Swagger Editor][swagger-editor] or [OpenAPI Generator][openapi-generator].

Note that Swagger's "Try it out" in-browser simulator creates valid curl requests, but the requests will fail due to [CORS][cors-docs] restrictions.

## Issues

If you encounter issues with these specifications or have feature requests, please [create an issue][issues].

[asyncapi-specification]: https://www.asyncapi.com/

[cors-docs]: https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS

[deepl-api]: https://www.deepl.com/pro-api

[issues]: https://github.com/DeepLcom/openapi/issues

[openapi-generator]: https://openapi-generator.tech/

[openapi-specification]: https://openapis.org/

[postman]: https://www.postman.com/

[swagger-editor]: https://editor.swagger.io/?url=https://raw.githubusercontent.com/DeepLcom/openapi/main/openapi.yaml
