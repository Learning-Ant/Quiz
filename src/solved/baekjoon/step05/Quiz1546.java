package solved.baekjoon.step05;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Quiz1546 {

	public static void main(String[] args) throws IOException {

		/*
		 * 세준이는 기말고사를 망쳤다. 세준이는 점수를 조작해서 집에 가져가기로 했다. 일단 세준이는 자기 점수 중에 최댓값을 골랐다.
		 * 
		 * 이 값을 M이라고 한다. 그리고 나서 모든 점수를 점수/M*100으로 고쳤다.
		 * 
		 * 예를 들어, 세준이의 최고점이 70이고, 수학점수가 50이었으면 수학점수는 50/70*100이 되어 71.43점이 된다.
		 * 
		 * 세준이의 성적을 위의 방법대로 새로 계산했을 때, 새로운 평균을 구하는 프로그램을 작성하시오.
		 */
		/*
		 * 기존의 평균을 구하는 식은 (a+b+c+...)/n
		 * 자기 점수의 최고점수가 만점인 것으로 환산하여 계산된 각 점수들은 a/M*100
		 * 새로운 평균의 식은 (a+b+c+...)*100/(n*M)
		 */
		
		// 11904KB	84ms
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int testCase = Integer.parseInt(br.readLine());
		int sum = 0, max=0;
		StringTokenizer st = new StringTokenizer(br.readLine().trim());
		for (int i = 0;i < testCase;i++) {
			int next = Integer.parseInt(st.nextToken());
			if (max<next) max=next;
			sum+=next;
		}
		bw.write(sum*100.0/(testCase*max)+"");
		
		bw.flush();
		bw.close();
		br.close();
	}

}
