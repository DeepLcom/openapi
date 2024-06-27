import click
from ruamel.yaml import YAML
import json


@click.command(
    "convert_to_json",
    help="Convert OpenAPI YAML to JSON ",
)
@click.argument("input")
@click.argument("output")
def main(input, output):
    yaml = YAML(typ="safe")
    with open(input, 'rt') as f:
        openapi = yaml.load(f)
    with open(output, 'w') as f:
        json.dump(openapi, f, indent=2)
        f.write("\n")  # Ensure trailing newline


if __name__ == "__main__":
    main()
