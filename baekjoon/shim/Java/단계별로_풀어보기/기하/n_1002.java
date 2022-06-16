package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.기하;

import java.io.*;

public class n_1002 {
    public static void main(String[] args)throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
        int n=Integer.parseInt(br.readLine());
        for(int i=0; i<n; i++){
            String st[]=br.readLine().split(" ");
            int r1=Integer.parseInt(st[2]), r2=Integer.parseInt(st[5]);
            double d=Math.sqrt(Math.pow(Integer.parseInt(st[0])-Integer.parseInt(st[3]), 2)+Math.pow(Integer.parseInt(st[1])-Integer.parseInt(st[4]),2));
            if(d==0 && r1==r2)
                bw.write(-1+"\n");
            else if(d>r1+r2 ||d<Math.abs(r1-r2))
                bw.write(0+"\n");
            else if(r1+r2==d || r1-r2==d || r2-r1==d)
                bw.write(1+"\n");
            else
                bw.write(2+"\n");
        }
        bw.flush();bw.close();
    }
}
