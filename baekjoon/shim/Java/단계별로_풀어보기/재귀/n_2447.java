package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.재귀;

import java.util.*;

public class n_2447 {
    public static char rect[][];
    public static void func(int x, int y, int n){
        if(n==1){
            rect[x][y]='*';
            return;
        }
        n/=3;
        for(int i=0; i<3; i++){
            for(int j=0; j<3; j++){
                if(i==1&&j==1)
                    continue;
                func(x+n*i,y+n*j,n);
            }
        }
    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        rect=new char[n][n];
        for(int i=0; i<n; i++)
            Arrays.fill(rect[i], ' ');
        func(0,0,n);
        for(int i=0; i<n; i++)
            System.out.println(rect[i]);
    }
}
