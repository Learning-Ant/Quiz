package solved.baekjoon.step10;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Quiz10872 {
	public static int factorial(int n) {
		if(n<=1) {
			return 1;
		}
		return n*factorial(n-1);
	}
	public static void main(String[] args) throws IOException {
		/*
		 * 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.
		 */
		
		/*
		 * 풀이
		 * 큰 숫자에서 하나씩 줄여가면서 재귀적인 호출이 일어나야 한다.
		 * 메소드 안에서 자기자신을 곱해가면서 호출되어야 하니
		 * return에 곱하면서 반환되고,
		 * 입력된 수가 0일경우(0!) 1이 반환되어야 하므로 if로 0일경우 1을 반환하도록 메소드를 만들어 준다.
		 */
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		System.out.println(factorial(Integer.parseInt(br.readLine())));
		
		br.close();
	}
}
