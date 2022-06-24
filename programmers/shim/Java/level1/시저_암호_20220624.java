package Study_2022.programmers.shim.Java.level1;

class Solution {
    public String solution(String s, int n) {
        String answer = "";
        for(int i=0; i<s.length(); i++){
            char c=s.charAt(i);
            if(c>='a'&&c<='z') answer+=c+n>'z'?(char)(c+n-26):(char)(c+n);
            else if(c>='A'&&c<='Z') answer+=c+n>'Z'?(char)(c+n-26):(char)(c+n);
            else answer+=' ';
        }
        return answer;
    }
}
