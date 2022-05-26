package Study_2022.baekjoon.shim.Java.알고리즘_분류.기본_수학_2;

import java.io.*;
import java.util.Arrays;

public class n_4948 {
    public static void main(String[] args)throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
        boolean arr[]=new boolean[2*123456+1];
        Arrays.fill(arr, true);
        arr[0]=arr[1]=false;
        
        for(int i=2; i<=Math.sqrt(123456*2)+1; i++){
            if(arr[i]){
                int j=2;
                while(i*j<=123456*2){
                    arr[i*j]=false;
                    j++;
                }
            }
        }

        int n=0;
        while((n=Integer.parseInt(br.readLine()))!=0){
            int count=0;
            for(int i=n+1; i<=n*2;i++){
                if(arr[i]) count++;
            }
            bw.write(count+"\n");
        }
        bw.flush();
        bw.close();
    }
}

// 자바로 푼 후에 파이썬으로 풀어보니 에라토스테네스의 체를 사용해서 푸는 것을 원하는 것 같아 다시 품
// import java.io.*;

// public class n_4948 {
//     public static void main(String[] args)throws IOException{
//         BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
//         BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
//         int n=0;
//         while((n=Integer.parseInt(br.readLine()))!=0){
//             int count=0;
//             for(int i=n+1; i<=n*2;i++){
//                 boolean b=true;
//                 for(int j=2; j<=Math.sqrt(i); j++){
//                     if(i%j==0){
//                         b=false;
//                         break;
//                     }
//                 }
//                 if(b) count++;
//             }
//             bw.write(count+"\n");
//         }
//         bw.flush();
//         bw.close();
//     }
// }