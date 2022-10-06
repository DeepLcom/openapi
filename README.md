# DeepL OpenAPI Specification

This project contains an [OpenAPI specification][openapi-specification] of the
[DeepL API][deepl-api], in [YAML](openapi.yaml) and [JSON](openapi.json)
formats.

You can use this specification to explore the API in tools like
[Postman][postman], or to auto-generate documentation, SDKs, and code libraries
using tools such as [Swagger Editor][swagger-editor] or
[OpenAPI Generator][openapi-generator].

Note that Swagger's "Try it out" in-browser simulator creates valid Curl
requests, the requests will fail due to [CORS][cors-docs] restrictions.

[Changelog](CHANGELOG.md)

If you encounter issues while using this OpenAPI specification or have feature
requests, please [create an issue][issues].

[deepl-api]: https://www.deepl.com/pro-api

[issues]: https://github.com/DeepLcom/openapi/issues

[openapi-specification]: https://openapis.org/

[openapi-generator]: https://openapi-generator.tech/

[postman]: https://www.postman.com/

[swagger-editor]: https://editor.swagger.io/?url=https://raw.githubusercontent.com/DeepLcom/openapi/main/openapi.yaml

[cors-docs]: https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS
