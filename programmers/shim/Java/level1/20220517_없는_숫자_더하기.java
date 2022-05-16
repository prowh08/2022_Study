import java.util.stream.*;
class Solution {
    public int solution(int[] numbers) {
        int answer = 45, sum=0;
        sum=IntStream.of(numbers).sum();
        return answer-sum;
    }
}