package solved.baekjoon.step08;

import java.util.Scanner;

public class Quiz2869 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		double a = sc.nextInt();
		double b = sc.nextInt();
		double v = sc.nextInt();
		int days = (int)(Math.ceil((v-a)/(a-b)))+1;
		System.out.println(days);
		sc.close();
	}

}
