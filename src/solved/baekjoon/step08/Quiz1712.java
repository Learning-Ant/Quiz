package solved.baekjoon.step08;

import java.util.Scanner;

public class Quiz1712 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int a=sc.nextInt(), b=sc.nextInt(), c=sc.nextInt();
		System.out.println(c>b?(int)(Math.floor(a/(c-b))+1):-1);
		sc.close();
	}

}
