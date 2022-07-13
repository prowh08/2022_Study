package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.누적_합;

import java.io.*;

public class n_16139 {
    public static void main(String[] args)throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
        String st=br.readLine();
        int arr[][]=new int[st.length()][26];
        arr[0][st.charAt(0)-'a']++;
        for(int i=1; i<st.length(); i++){
            for(int j=0; j<26; j++)
                arr[i][j]+=((st.charAt(i)-'a')==j?1:0)+arr[i-1][j];
       }
        int n=Integer.parseInt(br.readLine());
        for(int i=0; i<n; i++){
            String str[]=br.readLine().split(" ");
            bw.write(arr[Integer.parseInt(str[2])][str[0].charAt(0)-97]
            -(Integer.parseInt(str[1])>0?arr[Integer.parseInt(str[1])-1][str[0].charAt(0)-97]:0)+"\n");
        }
        bw.flush();bw.close();
    }
}