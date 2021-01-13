package solved.baekjoon.step01;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Quiz1000 {

	public static void main(String[] args) throws IOException {

		
	/*
	 * 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
	 */
	/*
	 * 두 정수이므로 br.readLine으로 읽으면 띄어쓰기로 split해준 후,
	 * int로 casting해 주고 더한 결과를 출력한다.
	 */
	// 11584KB 80ms
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	String[] s = br.readLine().split(" ");
	BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	int answer = Integer.parseInt(s[0])+Integer.parseInt(s[1]);
	
	bw.write(String.valueOf(answer));
	bw.flush();
	bw.close();
	br.close();
	}

}
