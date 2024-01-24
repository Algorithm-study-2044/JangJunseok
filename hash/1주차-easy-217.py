class Solution(object):
    def containsDuplicate(self, nums):
        hash_table = {}

        for item in nums:
            if item in hash_table:
                return True
            else:
                hash_table[item] = True

        return False