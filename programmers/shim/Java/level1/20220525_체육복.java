package Study_2022.programmers.shim.Java.level1;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = 0;
        int s[]=new int[n];
        for(int i=0; i<lost.length; i++)
            s[lost[i]-1]--;
        for(int i=0; i<reserve.length; i++)
            s[reserve[i]-1]++;
        for(int i=0; i<n; i++){
            if(s[i]==-1){
                if(i!=0&&s[i-1]>0){
                    s[i]++;
                    s[i-1]--;
                }else if(i!=s.length-1&&s[i+1]>0){
                    s[i]++;
                    s[i+1]--;
                }
            }
        }
        for(int i=0; i<n; i++)
            if(s[i]>=0) answer++;
        return answer;
    }
}
