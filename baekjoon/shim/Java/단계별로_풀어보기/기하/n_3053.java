package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.기하;

import java.util.*;

// public class n_3053 {
//     public static void main(String[] args){
//         Scanner sc=new Scanner(System.in);
//         int n=sc.nextInt();
//         System.out.println(String.format("%.6f", Math.pow(n,2)*Math.PI));
//         System.out.println(String.format("%.6f",Math.pow(n,2)*2));
//     }
// }

//리벤지전

public class n_3053 {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        System.out.println(String.format("%.6f\n%.6f", Math.pow(n,2)*Math.PI, Math.pow(n,2)*2));
    }
}
