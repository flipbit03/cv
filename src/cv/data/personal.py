from pydantic import HttpUrl

from cv.models import Personal

PERSONAL = Personal(
    name="Carlos Eduardo Coelho",
    title="Staff Software Engineer · Backend · LLM Tooling · Infra",
    location="Rio de Janeiro, Brazil",
    email="cadu.coelho@gmail.com",
    github=HttpUrl("https://github.com/flipbit03"),
    linkedin=HttpUrl("https://www.linkedin.com/in/carlos-eduardo-flipbit03/"),
    summary="""
Staff Software Engineer with extensive Linux fluency and a deep bench across Python, Rust, and C.
I solve hard backend problems (distributed systems, data pipelines, async services, infra) and ship them with the testing, type safety,
and documentation that make them durable.
I mentor the engineers I work with, and I'm a big fan and contributor to the Open Source movement.
""",
    epigraph="Small minds try to form religions, the great ones just want better routes up the mountain.",
    epigraph_attribution="Alan Kay",
)
