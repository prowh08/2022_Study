package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.그리디_알고리즘;
import java.util.*;

public class n_1541 {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        String st[]=sc.nextLine().split("-");
        int sum=0;
        for(int i=0; i<st.length; i++){
            String str[]=st[i].split("\\+");
            for(int j=0; j<str.length; j++){
                if(i==0)
                    sum+=Integer.parseInt(str[j]);
                else
                    sum-=Integer.parseInt(str[j]);
            }
        }
        System.out.println(sum);
    }    
}
