package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.정렬;

import java.util.*;

public class n_2108 {
    public static void main(String[]args){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt(), sum=0,answer=0, arr[]=new int[n];
        HashMap<Integer, Integer>map=new HashMap<>();
        for(int i=0; i<n; i++){
            arr[i]=sc.nextInt();
            map.put(arr[i], map.getOrDefault(arr[i], 0)+1);
            sum+=arr[i];
        }
        Arrays.sort(arr);
        int max = Collections.max(map.values());
		ArrayList<Integer> arrayList = new ArrayList<>();
		for (Map.Entry<Integer, Integer> m : map.entrySet()) {
			if (m.getValue() == max)
				arrayList.add(m.getKey());
		}
		Collections.sort(arrayList);
        if (arrayList.size() > 1)
            answer= arrayList.get(1);
		else 
            answer= arrayList.get(0);
        System.out.println(Math.round((double)sum/n)+"\n"+arr[n/2]+"\n"+answer+"\n"+(arr[n-1]-arr[0]));
    }
}
