"""
TODO: wire the StateGraph.

Sketch:

    from langgraph.graph import StateGraph, END
    from .state import GraphState
    from . import nodes

    graph = StateGraph(GraphState)
    graph.add_node("route", nodes.route)
    graph.add_node("retrieve_structured", nodes.retrieve_structured)
    graph.add_node("retrieve_semantic", nodes.retrieve_semantic)
    graph.add_node("grade_documents", nodes.grade_documents)
    graph.add_node("generate", nodes.generate)
    graph.add_node("verify", nodes.verify)

    graph.set_entry_point("route")
    graph.add_conditional_edges("route", <routing fn>, {
        "structured": "retrieve_structured",
        "semantic": "retrieve_semantic",
        "both": "retrieve_structured",  # then fan into semantic too
    })
    # ... grade_documents conditionally loops back or proceeds to generate
    # ... generate -> verify -> END

Think hard about the conditional edge after grade_documents — that's the
actual "agentic" part of this project, not boilerplate to copy.
"""
