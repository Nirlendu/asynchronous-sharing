from py2neo import Graph

def get_expressions(
        people,
        streams,
):
    graph = Graph()
    # expressions = graph.cypher.stream(
    #                  "MATCH (n:ExpressionGraph) -[:IN_TOPIC]->(Topic{name:'naarada'}), (a:Person{person_id: '" + request.session[
    #                      'person_id'] + "'})-[:EXPRESSED]->(n) RETURN n");

    return None