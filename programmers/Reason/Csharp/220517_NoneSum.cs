using System;

public class Solution {
 public int solution(int[] numbers) {
  int answer = ((1 + 9) * 9) / 2;
  foreach(var x in numbers)
   answer -= x;
  return answer;
 }
}