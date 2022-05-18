package Study_2022.baekjoon.shim.Java.알고리즘_분류.함수;

public class n_4673{
    public static void main(String[] args){
        boolean arr[]=new boolean[10100];
        for(int i=1; i<=10000; i++){
            int num=i, value=i;
            while(num!=0){
                value+=num%10;
                num/=10;
            }
            arr[value]=true;
        }
        for(int i=1; i<=10000; i++){
            if(arr[i]==false)
                System.out.println(i);
        }
    }
}