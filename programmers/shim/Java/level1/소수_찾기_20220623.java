package Study_2022.programmers.shim.Java.level1;

import java.util.*;
class Solution {
    public int solution(int n) {
        int answer = 0;
        boolean arr[]=new boolean[n+1];
        Arrays.fill(arr,false);
        for(int i=2; i<=n; i++){
            for(int j=2*i; j<=n; j+=i){
                if(arr[j]==true) continue;
                arr[j]=true;
            }
        }
        for(int i=2; i<=n; i++){
            if(arr[i]==false)
                answer++;
        }
        return answer;
    }
}