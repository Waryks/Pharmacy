from Domain.MedicineValidator import MedicineValidator
from Repository.RepositoryGeneric import RepositoryGeneric
from Services.ServicesMedicine import ServicesMedicine
from Services.ServicesClientCard import ServicesClientCard
from Services.ServicesTransaction import ServicesTransaction
from UserInterface.Console import Console
from Tests.RepositoryTests import runRepositoryTests
from Tests.DomainTests import runDomainTests


repository = RepositoryGeneric("medicinesFile", "cardsFile", "transactionsFile")

medValidator = MedicineValidator()

medService = ServicesMedicine(repository, medValidator)
clientCardService = ServicesClientCard(repository)
transactionService = ServicesTransaction(repository)

console = Console(medService, clientCardService, transactionService)
runRepositoryTests()
runDomainTests()



console.runConsole()
