# Massachusetts Institute of Technology
# MAS.500 Assignment 1
#
# Level: Intermediate
# To be used with the provided election_results_test.txt
# @author Alexandros Charidis, charidis@mit.edu

class ElectionResults:
    def __init__(self, filename):
        self.filename = filename

    def load(self):
        self.file = open(self.filename, 'r')
        self.all_lines = self.file.readlines()

    def states(self):
        all_names = []
        for line in self.all_lines:
            columns = line.split(',')
            all_names.append(columns[1])
        return all_names[1:]

    def state_count(self):
        return len(self.states())


    # Adds the names of the two candidates in a list
    #
    # @return False if file has not been read and its
    #         contents have not been stored
    def addNamesOfCandidates(self):
        try:
            print len(self.all_lines)
        except AttributeError:
            print "ElectionResults: Load the file first"
            return False
        
        # list to store names of candidates
        self.candidates = []
        # read first line of txt file and separate
        # strings with provided coma delimiter
        firstLine = self.all_lines[0].split(',')
        
        # assumes that name of candidate is separated
        # by one space from the word "vote" and that
        # there are only two candidates
        #
        # check election_results.txt
        
        self.candidates.append((firstLine[3].split(' '))[0])
        self.candidates.append((firstLine[5].split(' '))[0])

        print "ElectionResults: Added two candidates\n"


    # Associates candidate names with votes using
    # a dictionary data structure
    #
    # @return false if candidates are not defined
    def addTotalVotesOfCandidates(self):
        try:
            print len(self.candidates)
        except AttributeError:
            print "ElectionResults: Call addNamesOfCandidates first"
            return False
        
        # get the names of the two candidates
        assert len(self.candidates) == 2
        candidateA = self.candidates[0]
        candidateB = self.candidates[1]

        # count the number of votes of each candidate
        candAVotes = 0
        candBVotes = 0
        for v in self.all_lines[1:]:
            candAVotes += int((v.split(','))[3])
            candBVotes += int((v.split(','))[5])

        # dictionary to associate candidates and votes
        self.votes = {}
        self.votes[candidateA] = candAVotes
        self.votes[candidateB] = candBVotes

        print "ElectionResults: Counted total votes of candidates\n"


    ### Get functions

    # Get the two names of the two candidates
    #
    # @return a list of candidates
    # @print the names of the candidates
    def getCandidates(self):
        print "Candidates: %s and %s \n" % (self.candidates[0], self.candidates[1])
        return self.candidates


    # Get the number of total votes for each candidate
    #
    # @return a dictionary with candidates and their votes
    # @print information about candidates and their votes
    def getTotalVotes(self):
        print "%s got %i votes, and %s got %i votes" % \
              (self.candidates[0], self.votes[self.candidates[0]], \
               self.candidates[1], self.votes[self.candidates[1]])
        return self.votes


    # Compares the values of variables candA and candB.
    # Assumes that they are comparable without testing.
    #
    # @return 1 if candA greater than candB, -1 if
    #         candA smaller than candB, 0 otherwise
    def compare(self, candA, candB):
        if self.votes[candA] > self.votes[candB]:
            return 1
        elif self.votes[candA] < self.votes[candB]:
            return -1
        else:
            return 0
    
    def getWinner(self):
        win = self.compare(self.candidates[0], self.candidates[1])
        if win > 0:
            print "Obama won..."
            return 'Obama'
        elif win < 0:
            print "Romney won..."
            return 'Romney'
        else:
            print "Tie..."
            return 0

    
    
