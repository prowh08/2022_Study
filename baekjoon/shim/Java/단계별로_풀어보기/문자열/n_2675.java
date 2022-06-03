package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.문자열;

import java.io.*;

public class n_2675 {
    public static void main(String[] args)throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
        int n=Integer.parseInt(br.readLine());
        for(int i=0; i<n; i++){
            String str[]=br.readLine().split(" ");
            for(int k=0; k<str[1].length(); k++){
                for(int j=0; j<Integer.parseInt(str[0]); j++)
                    bw.write(str[1].charAt(k));
            }
            bw.write("\n");
        }
        bw.flush();
    }
}
