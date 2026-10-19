"""
TODO: implement each node as a function(state) -> partial state update.

route(state)
  Classify the question: structured / semantic / both.
  Keep the prompt tight and give it a few worked examples of each kind of
  question from the README scenario.

retrieve_structured(state)
  Translate the question into a pandas/SQL query over the incident data
  and run it. Start naive (an LLM call that writes the query), then
  tighten with validation once you see it misbehave.

retrieve_semantic(state)
  Vector search over the manual chunks. Consider metadata filtering by
  equipment type if the question names one.

grade_documents(state)
  Score whether retrieved context actually answers the question. On a low
  score, signal a retry (re-route or rephrase) rather than generating on
  weak context. Remember to bound retries using state.retry_count.

generate(state)
  Produce the answer, citing source filename/page or incident ID per
  claim.

verify(state)
  Cheap groundedness check: does the answer actually follow from the
  retrieved context? Flag or revise if not.
"""
