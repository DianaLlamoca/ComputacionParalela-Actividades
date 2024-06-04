 Implementa una versión simplificada del algoritmo de consenso Paxos en Python.

# Codigo base
import random

class Proposer:
    def __init__(self, id, acceptors):
        self.id = id
        self.acceptors = acceptors

    def propose(self, value):
        proposal_number = random.randint(1, 100)
        promises = 0
        for acceptor in self.acceptors:
            if acceptor.promise(proposal_number):
                promises += 1

        if promises > len(self.acceptors) // 2:
            for acceptor in self.acceptors:
                acceptor.accept(proposal_number, value)
            return True
        return False

class Acceptor:
    def __init__(self, id):
        self.id = id
        self.promised_proposal = 0
        self.accepted_proposal = 0
        self.accepted_value = None

    def promise(self, proposal_number):
        if proposal_number > self.promised_proposal:
            self.promised_proposal = proposal_number
            return True
        return False

    def accept(self, proposal_number, value):
        if proposal_number >= self.promised_proposal:
            self.accepted_proposal = proposal_number
            self.accepted_value = value

# Ejemplo de uso
acceptors = [Acceptor(i) for i in range(3)]
proposer = Proposer(1, acceptors)

if proposer.propose("value1"):
    print("Proposal accepted")
else:
    print("Proposal rejected")
