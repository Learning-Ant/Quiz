package solved.baekjoon.step10;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Quiz10870 {
	public static int p(int n) {
		if(n == 0) return 0;
		if(n == 1) return 1;
		return p(n - 2)+p(n - 1);
	}
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		System.out.println(p(Integer.parseInt(br.readLine())));
		
		br.close();
	}

}
