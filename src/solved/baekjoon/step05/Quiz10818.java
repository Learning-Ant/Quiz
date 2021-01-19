package solved.baekjoon.step05;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Quiz10818 {

	public static void main(String[] args) throws IOException {
		// N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

		/*
		 * 3가지 방법으로 풀어봤다.
		 * 1. 배열
		 * 먼저 배열로 입력된 값들을 받아 Arrays.sort() 메소드로 정렬하는 방법으로 문제를 풀었다.
		 * 이 방법같은 경우에는 sort()메소드의 알고리즘으로 인해 다른 방법들과 달리 시간에서 큰 차이를 보인다.
		 * sort()메소드의 구현 방식은 정렬 알고리즘 중 Quick sort를 이용한 것으로 알고있다.
		 * Quick sort같은 경우 여러 정렬 알고리즘 중 가장 빠르다고 알려진 분할 정복을 이용한 알고리즘이지만,
		 * 단순히 숫자를 비교하고 대입하는 방법에 비해 상당한 시간이 걸린다는 점을 알 수 있었다.
		 * 
		 * 2. while
		 * 단순히 최대, 최소인 값을 구해야 하는 경우에는 정렬을 쓰지 않아도 구현이 가능하다.
		 * 이럴 경우 1번의 방법보다 훨씬 빠른 속도를 보인다. 단순히 값을 비교하고, 대입하는 과정이기 때문이다.
		 * 
		 * 3. for
		 * 2번의 방법보다 조금 더 빠른 결과를 보였다.
		 * 이는 2번의 경우 루프를 돌 때 마다 StringTokenizer의 메소드 hasMoreTokens()를 호출하기 때문인 것으로 보인다.
		 * 루프를 실행할 때마다 이 루프를 한 번 더 실행해야하는 지 판단하기 위해 메소드를 매번 불러와야하기 때문인데
		 * for 같은 경우에는 딱 정해진 횟수만큼 반복하기 때문에 좀 더 적은 시간이 걸리는 것으로 보인다.
		 */
		
		/*
		 * 배열로 받아서 처리한다.
		 */
		// 128676KB	1008ms
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int testCase = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine().trim());
		
		int[] numList = new int[testCase];
		for (int i = 0 ; i<testCase ; i++) {
			numList[i] = Integer.parseInt(st.nextToken());
		}
		Arrays.sort(numList);
		bw.write(numList[0] + " " + numList[testCase-1]);
		
		/*
		 * 배열을 안써도 최솟값, 최댓값을 구할 수 있다.
		 */
		// 108436KB	468ms

		int min=Integer.parseInt(st.nextToken()), max = min;
		int next;
		while(st.hasMoreTokens()) {
			next = Integer.parseInt(st.nextToken()); 
			if(min>next) min=next;
			if(max<next) max=next;
		}
		bw.write(min+" "+max);
		
		/*
		 * 배열을 쓰지않고 for문으로 처리
		 */
		// 116476KB	420ms
		min=Integer.MAX_VALUE;
		max=Integer.MIN_VALUE;
		for(int i=0;i<testCase;i++) {
			next = Integer.parseInt(st.nextToken());
			if(min>next) min=next;
			if(max<next) max=next;
		}
		bw.write(min+" "+max);
		
		bw.flush();
		bw.close();
		br.close();
	}

}
