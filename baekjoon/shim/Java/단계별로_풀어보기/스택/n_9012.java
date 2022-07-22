package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.스택;

import java.io.*;
import java.util.*;

public class n_9012 {
    public static void main(String[] args)throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
        int n=Integer.parseInt(br.readLine());
        for(int i=0; i<n; i++){
            Stack<Character>stack=new Stack<>();
            boolean b=false;
            String st=br.readLine();
            for(int j=0; j<st.length(); j++){
                if(st.charAt(j)=='(')
                    stack.add('(');
                else{
                    if(stack.empty()){
                        b=true;
                        break;
                    }
                    else
                        stack.pop();
                }
            }
            if(b||!stack.empty())
                bw.write("NO\n");
            else
                bw.write("YES\n");
        }
        bw.flush();bw.close();
    }
}
