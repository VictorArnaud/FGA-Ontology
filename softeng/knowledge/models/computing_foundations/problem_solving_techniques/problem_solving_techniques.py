from core import Query, Sesame
from .definition_of_problem_solving import DefinitionOfProblemSolving


class ProblemSolvingTechniques(object):
    """
    Topic: Problem Solving Techniques
    """

    DEFINITION_OF_PROBLEM_SOLVING = 0
    FORMULATING_THE_REAL_PROBLEM = 1
    ANALYZE_THE_PROBLEM = 2
    DESIGN_A_SOLUTION_SEARCH_STRATEGY = 3
    PROBLEM_SOLVING_USING_PROGRAMS = 4

    def __init__(self):
        """
        Create a topic.
        """

        result = self.get_information()

        self.title = result['title']['value']

    def get_information(self):
        """
        Get the information from triple store
        """

        query = """
            PREFIX es: <http://www.semanticweb.org/ontologies/2018/Software_Engineering/>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>

            SELECT DISTINCT ?title
            WHERE {
              es:Problem_Solving_Techniques dc:title ?title
            }
        """

        result = Query.run(Sesame.endpoint, query)

        return result[0]

    def get_subtopic(self, subtopic):
        """
        Get a specific subtopic.
        """

        if subtopic == self.DEFINITION_OF_PROBLEM_SOLVING:
            return DefinitionOfProblemSolving()
        else:
            return None