package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.정수론_및_조합론;

import java.io.*;

public class n_1010 {
    public static void main(String[] args)throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
        int T=Integer.parseInt(br.readLine());
        for(int i=0; i<T; i++){
            String st[]=br.readLine().split(" ");
            int n=Integer.parseInt(st[0]),m=Integer.parseInt(st[1]);
            int max=Math.max(n,m), min=Math.min(n,m);
            long result=1;
            for(int j=max; j>Math.max(min,max-min); j--)
                result*=j;
            for(int j=2; j<=Math.min(min,max-min); j++)
                result/=j;
            bw.write(result+"\n");
        }
        bw.flush();bw.close();
    }
}
