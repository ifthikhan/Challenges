#!/usr/bin/env python
# encoding: utf-8

"""
Problem: Write a function to find overall winner in a tournament for teams when
supplied list of matches games played.
"""

import unittest
import math
from collections import namedtuple


class TournamanentResultProcessor(object):

    def __init__(self, matches):
        self.matches = matches
        self.teams_n_wins = self.process_input(matches)

    def process_input(self, matches):
        teams_n_wins = {}
        for match in matches:
            team1, team2 = match.teams
            if not teams_n_wins.has_key(team1):
                teams_n_wins[team1] = 0
            if not teams_n_wins.has_key(team2):
                teams_n_wins[team2] = 0
            teams_n_wins[match.winner] += 1
        return teams_n_wins

    def find_winner(self):
        max_wins = None
        max_win_team = None
        for team, wins in self.teams_n_wins.iteritems():
            if max_wins is None or wins > max_wins:
                max_wins = wins
                max_win_team = team
        return max_win_team

    def validate(self):
        num_teams = self.teams_n_wins
        # The number of teams participating should be even so that every team
        # in the first round can have an opponent.
        if num_teams & 1:
            return False

        # The total number of matches played should be equal to the total
        # number of nodes in a binary tree with leaf nodes n
        total_matches_played =  sum(self.teams_n_wins.values())
        expected_total = num_teams * 2 - 1
        if total_matches_played != expected_total:
            return False

        # Lets check the tournament table
        num_matches_played_sorted = sorted(self.teams_n_wins.values(),
                                           reversed=True)
        # Champion should play height of a binary tree
        height = int(math.floor(math.log(total_matches_played, 2)))
        # TODO: The number of matches played by each team can be validated using the
        # properties of binary tree

        # TODO: Check  that the loosing teams have never clibed up the ladder
        return True











class TestTournamentResultProcessor(unittest.TestCase):

    """Testcase for tournament results processor"""

    def setUp(self):
        Match = namedtuple("Match", ["teams", "winner"])

        matches = []
        matches.append(Match(teams=["A", "B"], winner="A"))
        matches.append(Match(teams=["C", "D"], winner="D"))
        matches.append(Match(teams=["E", "F"], winner="F"))
        matches.append(Match(teams=["G", "H"], winner="G"))

        matches.append(Match(teams=["A", "D"], winner="A"))
        matches.append(Match(teams=["F", "G"], winner="F"))

        matches.append(Match(teams=["F", "A"], winner="A"))
        self.matches = matches

    def test_find_winner(self):
        processor = TournamanentResultProcessor(self.matches)
        self.assertEqual("A", processor.find_winner())


if __name__ == '__main__':
    unittest.main()
