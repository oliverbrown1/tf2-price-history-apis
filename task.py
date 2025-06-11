import heapq

# Basic function + Input validation
def fill_bottles(queue, num_taps):

    # validation check - is queue an array, does it take only non-negative integers, and is num_taps a positive integer
    if not type(queue) is list:
        raise TypeError("queue should be an array!")
    if not all(type(i) is int and  i >= 0 for i in queue):
        raise TypeError("queue should only contain non-negative integers!")
    if (not type(num_taps) is int) or (num_taps <= 0):
        raise TypeError("num_taps should be a positive integer!")
    
    # priority queue based approach, keep the shortest accumulated queue time at the beginning of the array (using heaps)
    queue_times = [bottle / 100 for bottle in queue]

    taps = [0] * num_taps
    heapq.heapify(taps)

    # for each user, just add the time taken to the shortest tap queue (or the free tap queue if at front of the queue) for the user to fill their bottle
    for t in queue_times:
        next_tap = heapq.heappop(taps)
        tap_total = next_tap + t
        heapq.heappush(taps, tap_total)

    # return the longest accumulated tap time
    # note that max of heaps is more efficient than taken nlargest 
    return max(taps)

# challenge 2
def challenge_2(queue, num_taps, walking_time):

    queue_times = [bottle / 100 for bottle in queue]

    taps = [0] * num_taps
    heapq.heapify(taps)

    for t in queue_times:
        next_tap = heapq.heappop(taps)
        # uses the second assumption
        # each user is at the start of the queue and when the person before them finishes, they walk over
        tap_total = next_tap + t + walking_time
        heapq.heappush(taps, tap_total)

    return max(taps)

# challenge 3
def challenge_3(queue, num_taps, tap_rates):

    if num_taps != len(tap_rates):
        raise ValueError("Must be same length")

    # uses heap of tuples instead, to keep track of each taps queue time and their tap rates
    taps = [(0, r) for r in tap_rates]
    heapq.heapify(taps)

    for t in queue:
        next_tap = heapq.heappop(taps)
        # calculate time taken for user based on the current tap they are assigned to
        tap_total = next_tap[0] + (t / next_tap[1])
        heapq.heappush(taps, (tap_total, next_tap[1]))

    return max(taps)[0]

'''
challenge 4:

No it is not possible, this is becuase the function behaves greedily by assigning the next user in the queue to the tap with the lowest wait time, without actually waiting for the taps to be free. In this way when the user is at the front of the queue it is assigned to the free tap.

Because of this, increasing the flow rate has only 2 cases. The output remains unchanged as the longest tap queue is unaffected, the assignment of users to this queue remains unchanged for example:

a queue of [100,200,100] and 2 taps with tap_rates [100, 100] has a completion time of 2 seconds

If we modify the tap rate to [1000, 100] the first user still goes to the first tap and second user to the second tap, hence the second queue is still the longest, taking 2 seconds again.

The only other case is that the time decreases because the longest queue does get shorter as the assignment of users in that queue is decreased, due to a different tap having a faster flow rate. If the longest queue tap was given a faster flow rate, that queue length will decrease, so the longest queue length must decrease (hence the output).

If it took longer to fill all the bottles, at least one users time to fill their bottle would increase, but is not possible if the flow rate is increased overall.
'''
