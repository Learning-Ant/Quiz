package solved.baekjoon.step01;

import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;

public class Quiz10171 {

	public static void main(String[] args) throws IOException {

		// 아래 예제와 같이 고양이를 출력하시오.
		// \    /\
		//  )  ( ')
		//	(  /  )
		//	 \(__)|
		
		// 예제를 복사 붙혀넣기하면 자동으로 줄바꿈(\n, new line)이나 라인의 처음으로 갈때(\r, carriage return)의
		// escape sequence를 첨가해준다.
		// 11292KB 72ms
		StringBuilder sb = new StringBuilder("\\    /\\\n" + 
				" )  ( ')\n" + 
				"(  /  )\n" + 
				" \\(__)|");
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		bw.write(sb.toString());
		bw.flush();
		bw.close();
		
		
		// 11384KB 72ms
		/*
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		bw.write("\\    /\\\n" + 
				" )  ( ')\n" + 
				"(  /  )\n" + 
				" \\(__)|");
		bw.flush();
		bw.close();
		*/
	}

}
