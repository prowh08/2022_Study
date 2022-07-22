package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.스택;

import java.io.*;
import java.util.*;

public class n_10828 {
    public static void main(String[] args)throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
        int n=Integer.parseInt(br.readLine());
        Stack<Integer>stack=new Stack<>();
        for(int i=0; i<n; i++){
            String st[]=br.readLine().split(" ");
            switch(st[0]){
                case "push":
                    stack.push(Integer.parseInt(st[1]));
                    break;
                case "pop":
                    bw.write((stack.empty()?-1:stack.pop())+"\n");
                    break;
                case "size":
                    bw.write(stack.size()+"\n");
                    break;
                case "empty":
                    bw.write((stack.empty()?"1":"0")+"\n");
                    break;
                default:
                    bw.write((stack.empty()?"-1":stack.peek())+"\n");
                    break;
            }
        }
        bw.flush();bw.close();
    }
}
