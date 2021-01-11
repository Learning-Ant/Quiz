package solved.baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Quiz10870 {

	public static int p(int n) {
		if(n==0) return 0;
		if(n==1) return 1;
		return p(n-2)+p(n-1);
	}
	
	public static void main(String[] args) throws IOException {
		/*
		 * 피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 그 다음 2번째 부터는 바로 앞 두
		 * 피보나치 수의 합이 된다. 이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다. n=17일때 까지 피보나치 수를 써보면
		 * 다음과 같다. 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987,
		 * 1597 n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.
		 */
		/*
		 * Quiz10872와 비슷한 경우이다.
		 * 먼저 피보나치 수열의 정의에 해당하는 a_0과 a_1의 값을 반환할 수 있도록 if로 해당 값을 정의해준다.
		 * 그 후 n번째 수열의 값은 n-1번째 수열과 n-2번째 수열의 합이므로
		 * 둘의 합을 리턴하면 결국 n값이 2가 될때까지 계속적으로 p()메소드를 호출하게 된다.
		 */
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		System.out.println(p(Integer.parseInt(br.readLine())));
		br.close();
	}

}
