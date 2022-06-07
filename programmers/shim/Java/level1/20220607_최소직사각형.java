package Study_2022.programmers.shim.Java.level1;

class Solution {
    public int solution(int[][] sizes) {
        int answer = 0, max_h=0, max_w=0;
        for(int i=0; i<sizes.length; i++){
            if(sizes[i][0]<sizes[i][1]){
                int num=sizes[i][0];
                sizes[i][0]=sizes[i][1];
                sizes[i][1]=num;
            }
            max_h=Math.max(max_h,sizes[i][0]);
            max_w=Math.max(max_w,sizes[i][1]);
        }
        answer=max_h*max_w;
        return answer;
    }
    /*다른 풀이
    public int solution(int[][] sizes) {
        int w=Math.max(sizes[0][0],sizes[0][1]), h=Math.min(sizes[0][0],sizes[0][1]);
        for(int i=1; i<sizes.length; i++){
            int max=Math.max(sizes[i][0],sizes[i][1]), min=Math.min(sizes[i][0],sizes[i][1]);
            w=Math.max(w,max); h=Math.max(h,min);
        }
        int answer = w*h;
        return answer;
    }
     */
}
