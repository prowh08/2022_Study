package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.정수론_및_조합론;

import java.util.*;

public class n_2004 {
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		long N=sc.nextInt(), M=sc.nextInt();
		long c_5=five_n(N)-five_n(N-M)-five_n(M);
		long c_2=two_n(N)-two_n(N-M)-two_n(M);
		System.out.println(Math.min(c_5, c_2));
	}
	public static long five_n(long num) {
		int count=0;
		while(num>=5) {
			count+=(num/5);
			num/=5;
		}
		return count;
	}
	public static long two_n(long num) {
		int count=0;
		while(num>=2) {
			count+=(num/2);
			num/=2;
		}
		return count;
	}
}
