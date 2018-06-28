from rdflib import URIRef, Literal, XSD

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
knowledge = "http://www.semanticweb.org/ontologies/2018/Knowledge/"

description = """
Programming involves design, writing, testing, debugging, and maintenance.
Design is the conception or invention of a scheme for turning a customer
requirement for computer software into operational software. It is the activity
that links application requirements to coding and debugging. Writing is the
actual coding of the design in an appropriate programming language.  Testing is
the activity to verify that the code one writes actually does what it is
supposed to do. Debugging is the activity to find and fix bugs (faults) in the
source code (or design). Maintenance is the activity to update, correct, and
enhance existing programs.
"""


class TheProgrammingProcess(object):
    """
    Subtopic: The Programming Process
    """

    def __init__(self, graph):
        """
        Create a subtopic.
        """

        graph.add((
            URIRef(knowledge + 'The_Programming_Process'),
            URIRef(rdfs + 'subClassOf'),
            URIRef(knowledge + 'Programming_Fundamentals'),
        ))
        graph.add((
            URIRef(knowledge + 'The_Programming_Process'),
            URIRef(dc + 'title'),
            Literal('The Programming Process', lang='en')
        ))
        graph.add((
            URIRef(knowledge + 'The_Programming_Process'),
            URIRef(dc + 'description'),
            Literal(description, datatype=XSD.string)
        ))
