package Study_2022.programmers.shim.Java.level1;

import java.util.*;

public class 같은_숫자는_싫어_20220613 {
    public int[] solution(int []arr) {
        ArrayList<Integer> list=new ArrayList<>();
        list.add(arr[0]);
        for(int i=1; i<arr.length; i++){
            if(arr[i]!=arr[i-1])
                list.add(arr[i]);
        }
        int[] answer = new int[list.size()];
        for(int i=0; i<list.size(); i++){
            answer[i]=list.get(i);
        }
        return answer;
    }
}
