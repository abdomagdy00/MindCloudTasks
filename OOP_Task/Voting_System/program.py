import collections

class VotingSystem:
    """
    A class to manage a simple voting system using OOP principles.
    This class uses encapsulation to protect its internal data.
    """
    def __init__(self):
        # Use a dictionary to store candidates and their vote counts.
        # This is a private attribute (indicated by __) for encapsulation.
        self.__candidates = collections.defaultdict(int)

    def add_candidate(self, candidate_name):
        """
        Adds a new candidate to the system.
        """
        if candidate_name not in self.__candidates:
            self.__candidates[candidate_name] = 0
            print(f"Candidate '{candidate_name}' has been added.")
        else:
            print(f"Candidate '{candidate_name}' already exists.")

    def remove_candidate(self, candidate_name):
        """
        Removes a candidate from the system.
        """
        if candidate_name in self.__candidates:
            del self.__candidates[candidate_name]
            print(f"Candidate '{candidate_name}' has been removed.")
        else:
            print(f"Candidate '{candidate_name}' does not exist.")

    def vote_to_candidate(self, candidate_name):
        """
        Casts a vote for a candidate.
        """
        if candidate_name in self.__candidates:
            self.__candidates[candidate_name] += 1
            print(f"Vote cast for '{candidate_name}'.")
        else:
            print(f"Error: Candidate '{candidate_name}' not found.")

    def display_winner(self):
        """
        Displays the winner(s) of the election.
        Handles the case of a tie.
        """
        if not self.__candidates:
            print("No candidates to display a winner.")
            return

        # Find the maximum number of votes
        max_votes = 0
        if self.__candidates:
            max_votes = max(self.__candidates.values())
        
        # Find all candidates with the maximum number of votes
        winners = [
            candidate for candidate, votes in self.__candidates.items()
            if votes == max_votes
        ]

        if len(winners) == 1:
            print(f"\nThe winner is: {winners[0]} with {max_votes} votes.")
        elif len(winners) > 1:
            print(f"\nIt's a tie! The winners are: {', '.join(winners)} with {max_votes} votes each.")

# --- Example of usage ---
if __name__ == "__main__":
    election = VotingSystem()

    # Add candidates
    election.add_candidate("Alice")
    election.add_candidate("Bob")
    election.add_candidate("Charlie")
    election.add_candidate("Alice") # Attempt to add an existing candidate

    # Cast votes
    print("\nCasting votes...")
    election.vote_to_candidate("Bob")
    election.vote_to_candidate("Alice")
    election.vote_to_candidate("Alice")
    election.vote_to_candidate("Bob")
    election.vote_to_candidate("Charlie")
    election.vote_to_candidate("Alice")
    election.vote_to_candidate("Dan") # Attempt to vote for a non-existent candidate

    # Display the winner
    election.display_winner()
    
    # Remove a candidate and display winner again
    print("\nRemoving Bob and displaying winner again...")
    election.remove_candidate("Bob")
    election.display_winner()

