class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        
        players.sort()
        trainers.sort()
        
        player_pointer = 0
        trainer_pointer = 0
        count = 0
        
    
        while player_pointer < len(players) and trainer_pointer < len(trainers):
            if players[player_pointer] <= trainers[trainer_pointer]:
                count += 1
                player_pointer += 1
            trainer_pointer += 1
        
        return count

        