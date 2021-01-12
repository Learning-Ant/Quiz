package solved.baekjoon.step01;

import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;

public class Quiz2557 {

	public static void main(String[] args) throws IOException {
		
		/*
		 * Quiz2557
		 * Hello World!를 출력하시오.
		 */
		
		// 1. Buffer 클래스를 이용해 "Hello World!" 출력						// 11276KB 72ms
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		bw.write("Hello World!");
		bw.flush();
		bw.close();
		
		// 2. println()메소드로 바로 출력										// 11376KB 72ms
		System.out.println("Hello World!");
		
		// 3. StringBuffer 생성자를 이용해 메모리에 값을 할당하고 호출하기		// 11224KB 68ms
		StringBuffer sb = new StringBuffer("Hello World!");	
		System.out.println(sb);
	}

}
