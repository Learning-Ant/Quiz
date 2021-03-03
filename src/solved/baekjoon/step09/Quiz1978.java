package solved.baekjoon.step09;

import java.util.Scanner;

public class Quiz1978 {
	public static boolean isPrimeFactor(int n) {
	      if(n==1) return false;
	      if (n==2||n==3)return true;
	      for(int i=2;i<n;i++){
	      if(n%i==0) return false;
	    }
	    return true;
	  }
	  public static void main(String[] args){
	    Scanner sc = new Scanner(System.in);
	    int n=sc.nextInt();
	    int count=0;
	    for(int i=0;i<n;i++){
	      if(isPrimeFactor(sc.nextInt())) count++;
	    }
	    System.out.println(count);
	    sc.close();
	  }

}
