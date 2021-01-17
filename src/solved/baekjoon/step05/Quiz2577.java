package solved.baekjoon.step05;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Quiz2577 {

	public static void main(String[] args) throws IOException {

		// 세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.
		// 예를 들어 A = 150, B = 266, C = 427 이라면 A × B × C = 150 × 266 × 427 = 17037300 이 되고,
		// 계산한 결과 17037300 에는 0이 3번, 1이 1번, 3이 2번, 7이 2번 쓰였다.
		
		/*
		 * 먼저 0~9까지 각각의 숫자가 몇 번 나왔는지 카운팅할 배열을 만들어 준다.
		 * 그 후 받아준 세 개의 숫자를 곱한 결과에서 각 자리의 숫자는
		 * 선언해준 배열의 인덱스 번호와 같다.
		 */
		
		// 11540KB	80ms
		int[] digit = new int[10];
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		long answer = Integer.parseInt(br.readLine());
		answer*=Integer.parseInt(br.readLine());
		answer*=Integer.parseInt(br.readLine());
		
		boolean isFinish = false;
		
		while(!isFinish) {
			digit[(int)answer%10]++;
			answer/=10;
			
			if (answer==0) isFinish=true;
		}
		
		for (int i=0;i<digit.length;i++) {
			
			bw.write(digit[i]+"\n");
		}
		
		bw.flush();
		bw.close();
		br.close();
	}

}
