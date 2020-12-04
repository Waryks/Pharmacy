from Repository.RepositoryGeneric import *


def test_RepositoryTransactionsFile():
    r = RepositoryGeneric('testsFile', 'testsFile', 'testsFile')
    t = Transaction(1, 2, 0, 2, "13.11.2019", "11:34", "Active")
    r.addTransaction(t)
    assert len(r.getAllTransactions()) == 1
    assert r.getAllTransactions()[0] == t
    t1 = Transaction(1, 1, 0, 2, "14.11.2019", "15:34", "Active")
    r.updateTransaction(t1)
    assert r.getAllTransactions()[0] == t1
    r.removeTransaction(t1)
    assert t1.getDeleteStatus() == "Inactive"
    f = open('testsFile', 'r+')
    f.truncate(0)  # need '0' when using r+


def test_RepositoryClientCardsFile():
    r = RepositoryGeneric('testsFile', 'testsFile', 'testsFile')
    cc = ClientCard(1, "Popescu", "Daniel", 5000904111232, "04.09.2000", "13.11.2019", "Active")
    r.addCard(cc)
    assert len(r.getAllCards()) == 1
    assert r.getAllCards()[0] == cc
    cc1 = ClientCard(1, "Filip", "Patrick", 5000904111232, "17.10.2000", "21.11.2019", "Active")
    r.updateCard(cc1)
    assert r.getAllCards()[0] == cc1
    r.removeCard(cc1)
    assert cc1.getDeleteStatus() == "Inactive"
    f = open('testsFile', 'r+')
    f.truncate(0)  # need '0' when using r+


def test_RepositoryMedicinesFile():
    r = RepositoryGeneric('testsFile', 'testsFile', 'testsFile')
    m = Medicine(1, "Zinnat 250g", "GlaxoSmithKline Manufacturing SpA", 30.0, True, "Active")
    r.addMed(m)
    assert len(r.getAllMeds()) == 1
    assert r.getAllMeds()[0] == m
    m1 = Medicine(1, "Zinnat 500g", "GlaxoSmithKline Manufacturing SpA", 20.0, False, "Active")
    r.updateMed(m1)
    assert r.getAllMeds()[0] == m1
    r.removeMed(m1)
    assert m1.getDeleteStatus() == "Inactive"
    f = open('testsFile', 'r+')
    f.truncate(0)  # need '0' when using r+


def runRepositoryTests():
    test_RepositoryTransactionsFile()
    test_RepositoryClientCardsFile()
    test_RepositoryMedicinesFile()
