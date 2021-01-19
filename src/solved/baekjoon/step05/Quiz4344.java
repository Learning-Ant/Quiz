package solved.baekjoon.step05;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.text.DecimalFormat;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Quiz4344 {

	public static void main(String[] args) throws IOException{

		/*
		 * 첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
		 * 
		 * 둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고,
		 * 
		 * 이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.
		 * 
		 * 소수점 셋째자리까지 구하라.
		 */
		
		/*
		 * 각 케이스마다 평균이 넘는 학생들의 수를 구하기 위해
		 * 케이스 별로 평균을 넘는 학생들의 수를 구해 준다.
		 * 결과를 출력하기 위해 StringBuilder를 사용한다.
		 */
		
		// 14368KB	136ms
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int testCase = Integer.parseInt(br.readLine());
		StringBuilder sb = new StringBuilder();
		sb.trimToSize();
		for (int i = 0; i<testCase ;i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int stdCount = Integer.parseInt(st.nextToken());
			double avg = 0;
			double percent = 0;
			
			List<Integer> scoreList = new ArrayList<Integer>();
			// 남은 토큰이 있을 때까지 list에 추가하고 avg를 계산하기 위해 합계를 구한다.
			while(st.hasMoreTokens()) {
				int next = Integer.parseInt(st.nextToken());
				scoreList.add(next);
				avg+=next;
			}
			avg/=stdCount;
			
			// 구한 avg로 평균을 넘는 학생들의 수를 구한다.
			for(int j : scoreList) {
				if(j>avg) percent++;
			}
			percent/=stdCount;
			
			sb.append(new DecimalFormat("0.000").format(percent*100)+"%\n");
		}
		
		bw.write(sb.toString());		
		
		bw.flush();
		bw.close();
		br.close();
		
	}

}
