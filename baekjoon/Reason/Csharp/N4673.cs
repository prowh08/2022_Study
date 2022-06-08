using System;
using System.Collections.Generic;

class Program{
  static void Main(string[] args){
      List<int> NotSelfs = new List<int>();
      for(int i = 0;IntegerByNatural(i)<=10000;i++){
          if(!NotSelfs.Contains(IntegerByNatural(i)))
              NotSelfs.Add(IntegerByNatural(i));
      }
      for(int i = 0;i<=10000;i++){
          if(!NotSelfs.Contains(i))
              Console.WriteLine(i);
      }
  }
  static int IntegerByNatural(int n){
      int divided = n;
      int fin = n;
      while(true){
          if(divided == 0) break;
          fin += (divided%10);
          divided /= 10;
      }
      return fin;
  }
};