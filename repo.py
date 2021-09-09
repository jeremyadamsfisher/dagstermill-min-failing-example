import dagstermill as dm
from dagster.utils import script_relative_path
from dagster import pipeline, repository, OutputDefinition, String, solid

hello = dm.define_dagstermill_solid(
    "hello",
    script_relative_path("hello.ipynb"),
    input_defs=[],
    output_defs=[OutputDefinition(String)]
)


@pipeline
def my_pipeline():
    hello()


@repository
def deploy_docker_repository():
    return [my_pipeline]
