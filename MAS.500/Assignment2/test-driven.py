# Verify that we can open and read the election results txt correctly
# Showing a "test-driven" style

from electionResults import ElectionResults
import unittest

class ElectionResultsTest(unittest.TestCase):

    def setUp(self):
        self.results = ElectionResults('election_results_test.txt')

    def testLoad(self):
        self.results.load()
        assert self.results!=None
        assert self.results.file!=None
        
    def testStateCount(self):
        self.results.load()
        state_count = self.results.state_count()
        assert state_count==2

    def testStates(self):
        self.results.load()
        names = self.results.states()
        assert len(names)==2
        assert names[0]=='Alaska'
        assert names[1]=='Alabama'

    def testAddNamesOfCandidates(self):
        self.results.load()
        self.results.addNamesOfCandidates()
        candidates = self.results.getCandidates()
        assert len(candidates) == 2
        assert candidates[0]=='Obama'
        assert candidates[1]=='Romney'

    def testAddTotalVotesOfCandidates(self):
        self.results.load()
        self.results.addNamesOfCandidates()
        self.results.addTotalVotesOfCandidates()
        votes = self.results.getTotalVotes()
        assert len(votes) == 2
        assert votes['Obama']!=None
        assert votes['Romney']!=None

    def testGetWinner(self):
        self.results.load()
        self.results.addNamesOfCandidates()
        self.results.addTotalVotesOfCandidates()
        assert self.results.getWinner() != None 
    
# if this file is run directly, run the tests
if __name__ == "__main__":
    unittest.main()
