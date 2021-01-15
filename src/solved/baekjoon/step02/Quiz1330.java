package solved.baekjoon.step02;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Quiz1330 {

	public static void main(String[] args) throws IOException{

		// 두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int result = Integer.compare(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
		
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		if (result == 0) {
			bw.write("==");
		} else if (result < 0) {
			bw.write("<");
		} else if (result > 0) {
			bw.write(">");
		}
		
		bw.flush();
		bw.close();
		br.close();
	}

}
