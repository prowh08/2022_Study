package Study_2022.programmers.shim.Java.level1;

public class 이상한_문자_만들기_20220704 {
    public String solution(String s) {
        String str[]=s.split(" ",-1);
        String answer = "";
        for(int i=0; i<str.length; i++){
            String st[]=str[i].split("");
            for(int j=0; j<str[i].length(); j++)
                answer+=j%2==0? st[j].toUpperCase():st[j].toLowerCase();
            if(i!=str.length-1)
                answer+=" ";
        }
        return answer;
    }
}
