package solved.baekjoon.step04;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Quiz10952 {

	public static void main(String[] args) throws IOException {

		// 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
		
		/*
		 * 종료 조건이 입력받은 두 수가 모두 0일 때이므로
		 * while-break를 이용해 푼다.
		 */
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		while(true) {
			StringTokenizer st = new StringTokenizer(br.readLine().trim());
			int n1=Integer.parseInt(st.nextToken()), n2=Integer.parseInt(st.nextToken());
			if(n1==0&&n2==0) {
				break;
			}
			bw.write(n1+n2+"\n");
		}
		bw.flush();
		bw.close();
		br.close();
	}

}
