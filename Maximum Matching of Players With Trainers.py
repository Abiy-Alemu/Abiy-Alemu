class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        
        players.sort()
        trainers.sort()

        count =0 
        pp = 0 # players_pointer
        tp  = 0 # trainers_pointer
        n = len(players)
        m  = len(trainers)
        

        while pp < n and tp < m:
            if players[pp] <= trainers[tp]:
                count  += 1
                pp += 1
            tp += 1

        return count


        