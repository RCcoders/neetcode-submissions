class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}  # Map to store: {character: its_most_recent_index}
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            current_char = s[right]
            
            # If the character is a duplicate and is inside our current window
            if current_char in char_map and char_map[current_char] >= left:
                # Slide the left boundary past the previous occurrence
                left = char_map[current_char] + 1
                
            # Update/Insert the character's newest position
            char_map[current_char] = right
            
            # Calculate the current window size and update max_length
            current_window_len = right - left + 1
            max_length = max(max_length, current_window_len)
            
        return max_length