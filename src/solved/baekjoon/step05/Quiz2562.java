package solved.baekjoon.step05;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Quiz2562 {

	public static void main(String[] args) throws IOException {

		/*
		 * 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
		 * 
		 * 예를 들어, 서로 다른 9개의 자연수
		 * 
		 * 3, 29, 38, 12, 57, 74, 40, 85, 61
		 * 
		 * 이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.
		 */
		/*
		 * 예시를 보면 각각의 입력이 라인으로 이루어지고 있다.
		 * 따라서 readLine()메소드로 하나하나씩 불러올 수 있다.
		 * 문제에서 9개의 서로 다른 숫자라고 총 숫자들의 개수를 명시했으므로
		 * 순회의 횟수가 명확하다.
		 * for문을 이용해 input의 값이 max의 값보다 클 경우만 선정하여
		 * 그 때가 몇 번째인지를 count에 저장하고 max의 값을 input으로 초기화시킨다.
		 * 그 후 해당 값들을 출력시켜준다.
		 */
		// 	11580KB	72ms
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int max=Integer.MIN_VALUE;
		int count=0;
		for(int i=0; i<9; i++) {
			int input = Integer.parseInt(br.readLine());
			if(max<input) {
				max=input;
				count=i;
			}
		}
		bw.write(max+"\n"+(count+1));
		bw.flush();
	}

}
