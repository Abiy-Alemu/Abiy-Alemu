import sys
def can_untangle_wires(sequence):
    minus_count = sequence.count('-')
    
    if minus_count % 2 == 0:
        return "Yes"
    else:
        return "No"


input = sys.stdin.read
sequence = input().strip()

print(can_untangle_wires(sequence))