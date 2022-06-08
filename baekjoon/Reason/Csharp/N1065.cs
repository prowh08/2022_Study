using System;

class Program{
    static void Main(string[] arg){
        int n = int.Parse(Console.ReadLine());
        Console.WriteLine(NumOfHan(n));
    }
    static int NumOfHan(int n){
        if(n<100){
            return n;
        }else if(n<110){
            return 99;
        }
        int total = 99;
        int fin = (n == 1000) ? 999 : n;
        int[] num = new int[3];
        for(int i = 111;i<=fin;i++){
            num[0] = i/100;
            num[1] = (i%100)/10;
            num[2] = i%10;
            if((num[0]-num[1])==(num[1]-num[2]))
                total++;
        }
        return total;
    }
};