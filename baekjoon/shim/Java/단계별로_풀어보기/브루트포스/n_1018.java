package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.브루트포스;

import java.io.*;

public class n_1018 {
	public static int func(int row, int col, String[] board) {
		String orgBoard[] = {"WBWBWBWB", "BWBWBWBW"};
		int whiteSol = 0;
		for(int i=0; i<8; i++) {
			int r = row + i;
			for(int j=0; j<8; j++) {
				int c = col + j;
				if(board[r].charAt(c) != orgBoard[r % 2].charAt(j))
					whiteSol++;
			}
		}
		return Math.min(whiteSol, 64 - whiteSol);
	}
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] st = br.readLine().split(" ");
		int r = Integer.parseInt(st[0]), c = Integer.parseInt(st[1]),min = Integer.MAX_VALUE;
		String board[] = new String[r];
		for(int i=0; i<r; i++)
			board[i] = br.readLine();
		for(int i=0; i<r - 7; i++) {
			for(int j=0; j<c - 7; j++) {
				int num = func(i, j, board);
				if(min > num)
					min = num;
			}
		}
		System.out.println(min);
	}
}
