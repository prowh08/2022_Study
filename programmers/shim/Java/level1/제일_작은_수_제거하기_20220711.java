package Study_2022.programmers.shim.Java.level1;

import java.util.Arrays;

public class 제일_작은_수_제거하기_20220711 {
    public int[] solution(int[] arr) {
        int count=0;
        int[] ans={-1};
        if(arr.length==1) return ans;
        else{
            int[] answer = new int[arr.length-1];
            int[] arr2=Arrays.copyOf(arr,arr.length);
            Arrays.sort(arr2);
            for(int i=0; i<arr2.length; i++){
                if(arr2[0]==arr[i])
                    continue;
                else{
                    answer[count]=arr[i];
                    count++;
                }
            }
            return answer;
        }
    }
}
