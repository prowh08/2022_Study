package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.집합과_맵;

import java.io.*;
import java.util.*;

public class n_1764 {
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
        String st[]=br.readLine().split(" ");
        ArrayList<String>list=new ArrayList<>();
        HashSet<String>set=new HashSet<>();
        for(int i=0; i<Integer.parseInt(st[0]); i++)
            set.add(br.readLine());
        for(int i=0; i<Integer.parseInt(st[1]);i++){
            String str=br.readLine();
            if(set.contains(str))
                list.add(str);
        }
        bw.write(list.size()+"\n");
        Collections.sort(list);
        for(int i=0; i<list.size(); i++)
            bw.write(list.get(i)+"\n");
        bw.flush();bw.close();
    }
}
