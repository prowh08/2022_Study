package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.기하;

// import java.io.*;

// public class n_1002 {
//     public static void main(String[] args)throws IOException{
//         BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
//         BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
//         int n=Integer.parseInt(br.readLine());
//         for(int i=0; i<n; i++){
//             String st[]=br.readLine().split(" ");
//             int r1=Integer.parseInt(st[2]), r2=Integer.parseInt(st[5]);
//             double d=Math.sqrt(Math.pow(Integer.parseInt(st[0])-Integer.parseInt(st[3]), 2)+Math.pow(Integer.parseInt(st[1])-Integer.parseInt(st[4]),2));
//             if(d==0 && r1==r2)
//                 bw.write(-1+"\n");
//             else if(d>r1+r2 ||d<Math.abs(r1-r2))
//                 bw.write(0+"\n");
//             else if(r1+r2==d || r1-r2==d || r2-r1==d)
//                 bw.write(1+"\n");
//             else
//                 bw.write(2+"\n");
//         }
//         bw.flush();bw.close();
//     }
// }

//리벤지전
import java.io.*;

public class n_1002 {
    public static void main(String[] args)throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
        int n=Integer.parseInt(br.readLine()), arr[]=new int[6], c=1;
        for(int i=0; i<n; i++){
            String st[]=br.readLine().split(" ");
            for(int j=0; j<6; j++)
                arr[j]=Integer.parseInt(st[j]);
            double d=Math.sqrt(Math.pow(Math.abs(arr[0]-arr[3]),2)+Math.pow(Math.abs(arr[1]-arr[4]),2));
            if(d==0&&arr[2]==arr[5])
                c=-1;
            else if(Math.abs(arr[2]-arr[5])<d&&d<arr[2]+arr[5])
                c=2;
            else if(arr[2]+arr[5]<d ||Math.abs(arr[2]-arr[5])>d)
                c=0;
            bw.write(c+"\n");
        }
        bw.close(); bw.close();
    }
}