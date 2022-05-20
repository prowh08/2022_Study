package Study_2022.programmers.shim.Java.level1;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        for(int i=0; i<nums.length-2; i++){
            for(int j=i+1; j<nums.length-1; j++){
                for(int k=j+1; k<nums.length; k++){
                    boolean b=false;
                    int num=nums[i]+nums[j]+nums[k];
                    for(int l=2; l<=Math.sqrt(num); l++){
                        if(num%l==0){
                            b=true;
                            break;
                        }
                    }
                    answer+=(b?0:1);
                }
            }
        }
        return answer;
    }
}