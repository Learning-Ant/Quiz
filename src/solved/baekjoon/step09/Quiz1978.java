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
		  
		  /*
			 * 주어진 수 N개 중에서 소수가 몇 개인지 찾아서
			 * 출력하는 프로그램을 작성하시오.
			 * 
			 * 예시)
			 * 4
			 * 1 3 5 7
			 * 
			 * 출력)
			 * 3
			 */
			/*
			 * 풀이
			 * 입력받은 수가 소수인지를 판단할 수 있는 메소드를 따로 만들어서
			 * main메소드에서 호출하는 방식으로 문제풀이를 진행했다.
			 * 
			 * 해당 풀이법의 문제는 입력되는 숫자가 크거나 많아질수록 시간소요가 커진다는 점이다.
			 * 문제의 조건이 그렇게 큰 범위와 많은 숫자가 입력되지 않으므로
			 * 정답의 조건에'만' 부합하는 풀이법이다.
			 */
			
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
