package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.집합과_맵;

import java.io.*;
import java.util.HashSet;

public class n_14425 {
    public static void main(String[] args)throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        String st[]=br.readLine().split(" ");
        HashSet<String> set=new HashSet<>();
        for(int i=0; i<Integer.parseInt(st[0]); i++)
            set.add(br.readLine());
        int count=0;
        for(int i=0; i<Integer.parseInt(st[1]); i++){
            String str=br.readLine();
            if(set.contains(str))
                count++;
        }
        System.out.println(count);
    }
}
