package Study_2022.programmers.shim.Java.level1;

import java.util.*;
class Solution {
    public int[] solution(int[] numbers) {
        int[] answer = {};
        HashSet<Integer>set=new HashSet<>();
        for(int i=0; i<numbers.length-1;i++){
            for(int j=i+1; j<numbers.length; j++){
                set.add(numbers[i]+numbers[j]);
            }
        }
        return set.stream().sorted().mapToInt(Integer::intValue).toArray();
    }
}