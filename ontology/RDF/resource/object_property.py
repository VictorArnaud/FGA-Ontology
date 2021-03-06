from rdflib import URIRef
from .prefix import rdfs, pp, rdf

subClassOf = URIRef(rdfs + 'subClassOf')
typeOf = URIRef(rdf + 'type')
hasCampus = URIRef(pp + 'hasCampus')
hasCourse = URIRef(pp + 'hasCourse')
hasExtensionActivitie = URIRef(pp + 'hasExtensionActivitie')
belongsTo = URIRef(pp + 'belongsTo')
hasPeriod = URIRef(pp + 'hasPeriod')
hasStructureCurricular = URIRef(pp + 'hasStructureCurricular')
hasType = URIRef(pp + 'hasType')
isInTheFlowOf = URIRef(pp + 'isInTheFlowOf')
isPartOf = URIRef(pp + 'isPartOf')
hasContent = URIRef(pp + 'hasContent')
hasRequired = URIRef(pp + 'hasRequired')
isRequiredOf = URIRef(pp + 'isRequiredOf')
