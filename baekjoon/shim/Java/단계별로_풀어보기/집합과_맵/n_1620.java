package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.집합과_맵;

import java.io.*;
import java.util.HashMap;

public class n_1620 {
    public static void main(String[] args)throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
        String st[]=br.readLine().split(" ");
        HashMap<String,String>map=new HashMap<>();
        for(int i=0; i<Integer.parseInt(st[0]); i++){
            String pkm=br.readLine();
            map.put(Integer.toString(i+1), pkm);
            map.put(pkm,Integer.toString(i+1));
        }
        for(int i=0; i<Integer.parseInt(st[1]); i++){
            bw.write(map.get(br.readLine())+"\n");
        }
        bw.flush();bw.close();
    }
}
