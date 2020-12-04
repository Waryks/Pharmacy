from Domain.Medicine import Medicine
from Domain.ClientCard import ClientCard
from Domain.Transaction import Transaction


def test_Medicine():
    m = Medicine(1, "Zinnat", "GlaxoSmithKline Manufacturing SpA", 30.0, True, "True")
    assert m.getID() == 1
    assert m.getName() == "Zinnat"
    assert m.getProducer() == "GlaxoSmithKline Manufacturing SpA"
    assert abs(m.getPrice() - 30) < 0.01
    assert m.getPrescription() is True
    m1 = Medicine(1, "Zinnat", "GlaxoSmithKline Manufacturing SpA", 30.0, True, "True")
    assert m1 == m
    m1.setPrice(2)
    assert m1 != m


def test_ClientCard():
    cc = ClientCard(1, "Popescu", "Daniel", 5000904111232, "04.09.2000", "13.11.2019", "True")
    assert cc.getID() == 1
    assert cc.getSurname() == "Popescu"
    assert cc.getForename() == "Daniel"
    assert cc.getCNP() == 5000904111232
    assert cc.getDateOfBirth() == "04.09.2000"
    assert cc.getRegistrationDate() == "13.11.2019"
    cc1 = ClientCard(1, "Popescu", "Daniel", 5000904111232, "04.09.2000", "13.11.2019", "True")
    assert cc1 == cc
    cc1.setForename("Patrick")
    assert cc1 != cc


def test_Transaction():
    t = Transaction(1, 2, 0, 2, "13.11.2019", "11:34", "True")
    assert t.getID() == 1
    assert t.getMedID() == 2
    assert t.getCardID() == 0
    assert t.getAmount() == 2
    assert t.getDate() == "13.11.2019"
    assert t.getClock() == "11:34"
    t1 = Transaction(1, 2, 0, 2, "13.11.2019", "11:34", "True")
    assert t1 == t
    t1.setMedID(3)
    assert t1 != t


def runDomainTests():
    test_ClientCard()
    test_Medicine()
    test_Transaction()





