"""
TODO: define the graph state (TypedDict or pydantic model).

Think about what needs to persist across nodes, e.g.:
  - question: str
  - route: Literal["structured", "semantic", "both"] | None
  - structured_results / semantic_results
  - grade: a relevance score or pass/fail
  - retry_count: int  (bound your self-correction loop!)
  - answer: str | None
  - citations: list[...]
"""
