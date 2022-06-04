package Study_2022.programmers.shim.Java.level1;

import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        int[] n1={1,2,3,4,5}, n2={2,1,2,3,2,4,2,5}, n3={3,3,1,1,2,2,4,4,5,5};
        int arr[]=new int[3];
        for(int i=0; i<answers.length; i++){
            if(answers[i]==n1[i%5]) arr[0]++;
            if(answers[i]==n2[i%8]) arr[1]++;
            if(answers[i]==n3[i%10]) arr[2]++;
        }
        ArrayList<Integer>list=new ArrayList<>();
        int max=Math.max(arr[0],Math.max(arr[1],arr[2]));
        for(int i=0; i<3; i++){
            if(arr[i]==max) list.add(i+1);
        }
        int[] answer = new int[list.size()];
        for(int i=0; i<list.size(); i++)
            answer[i]=list.get(i);
        return answer;
    }
}
