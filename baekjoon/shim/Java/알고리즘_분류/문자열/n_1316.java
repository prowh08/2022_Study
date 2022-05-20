package Study_2022.baekjoon.shim.Java.알고리즘_분류.문자열;

import java.io.*;

public class n_1316 {
    public static void main(String[] args)throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int n=Integer.parseInt(br.readLine()), count=0;
        for(int i=0; i<n; i++){
            String st=br.readLine();
            int arr[]=new int[26];
            for(int j=1; j<st.length(); j++){
                if(st.charAt(j-1)!=st.charAt(j)){
                    if(arr[st.charAt(j)-'a']==1){
                        count++;
                        break;
                    }
                    arr[st.charAt(j-1)-'a']=1;
                }
            }
        }
        System.out.println(n-count);
    }
}
