package Study_2022.programmers.shim.Java.level1;

import java.util.*;
class Solution {
    public int solution(int[] nums) {
        HashSet<Integer>set=new HashSet<>();
        for(int i=0; i<nums.length; i++)
            set.add(nums[i]);
        int answer = Math.min(set.size(), nums.length/2);
        return answer;
    }
}
