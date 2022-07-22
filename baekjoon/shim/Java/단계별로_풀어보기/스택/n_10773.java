package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.스택;

import java.io.*;
import java.util.*;

public class n_10773 {
    public static void main(String[] args)throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int n=Integer.parseInt(br.readLine()), sum=0;
        Stack<Integer>stack=new Stack<>();
        for(int i=0; i<n; i++){
            int num=Integer.parseInt(br.readLine());
            if(num==0)
                sum-=stack.pop();
            else{
                stack.add(num);
                sum+=num;
            }
        }
        System.out.println(sum);
    }
}
