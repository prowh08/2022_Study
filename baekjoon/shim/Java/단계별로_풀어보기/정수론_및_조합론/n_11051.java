package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.정수론_및_조합론;

import java.util.*;

public class n_11051 {
	public static int [][]dp=new int[1001][1001];
	public static int Pas(int N, int K) {
		if(N==K||K==0)
			return 1;
		if(dp[N][K]>0)
			return dp[N][K];
		dp[N][K]=Pas(N-1, K-1)+Pas(N-1,K);
		return dp[N][K]%10007;
	}
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int N=sc.nextInt(), K=sc.nextInt();
		System.out.println(Pas(N,K));
	}
}