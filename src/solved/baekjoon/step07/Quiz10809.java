package solved.baekjoon.step07;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Quiz10809 {

	public static void main(String[] args) throws IOException {

		/*
		 * 알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어
		 * 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.
		 */
		/*
		 * indexOf의 특성활용
		 * indexOf()메소드는 문자열에서 찾는 문자가 존재하지 않을 경우 -1을 반환한다.
		 * 이를 활용해 문제를 풀어본다.
		 */
		// 11572KB	76ms
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringBuilder sb = new StringBuilder();
		sb.trimToSize();
		String word = br.readLine();
		// 97~122
		for(int i=97;i<123;i++) {
			sb.append(word.indexOf((char)i)+" ");
		}
		bw.write(sb.toString().trim());
		bw.flush();
		bw.close();
		br.close();
	}

}
