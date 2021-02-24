package solved.baekjoon.step07;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Quiz2675 {

	public static void main(String[] args) throws IOException {

		
		//문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오.
		// 즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. S에는 QR Code "alphanumeric" 문자만 들어있다.

		//QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int testCase = Integer.parseInt(br.readLine());
		int count = 0;
		StringBuilder sb=new StringBuilder();
		for(int t = 0 ; t<testCase ; t++) {
			StringTokenizer st = new StringTokenizer(br.readLine()," ");
			count = Integer.parseInt(st.nextToken());
			String[] strArray = st.nextToken().split("");
			for (int i = 0 ; i<strArray.length ; i++) {
				for ( int j = 0 ; j<count ; j++) {
					sb.append(strArray[i]);
				}
			}
			sb.append(" ");
		}
		String[] results = sb.toString().split(" ");
		for (int i = 0 ; i<results.length ; i++) {
			System.out.println(results[i]);
		}
	}

}
