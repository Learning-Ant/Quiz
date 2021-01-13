package unsolved.baekjoon.step01;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.nio.file.Paths;

public class Quiz10172 {

	public static void main(String[] args) throws IOException {

		
		/*
		 * Quiz10171과 같은 유형의 문제이다.
		 * 좀 더 색다른 방식으로 파일을 만들어 그 안의 내용으로 원하는 모양을 입력하고
		 * 만든 파일의 내용을 읽어와 콘솔에 출력하는 방법으로 풀어본다.
		 */
		String path = Paths.get("").toAbsolutePath().toString();
		File file = new File(path+"/Quiz10172.txt");
		BufferedWriter bw1 = new BufferedWriter(new FileWriter(file));
		
		bw1.write("|\\_/|\r\n" + 
				  "|q p|   /}\r\n" + 
				  "( 0 )\"\"\"\\\r\n" + 
				  "|\"^\"`    |\r\n" + 
				  "||_/=\\\\__|");
		BufferedReader br = new BufferedReader(new FileReader(file));
		System.out.println(file.toPath());
		
		BufferedWriter bw2 = new BufferedWriter(new OutputStreamWriter(System.out));
		StringBuffer sb = new StringBuffer();
		
		while(true) {
			char[] cbuf = new char[10];
			int state = br.read(cbuf);
			if(state==-1) {
				break;
			} else {
				sb.append(cbuf);
			}
		}
		sb.append("asdf");
		
		System.out.println(sb);
		if(file.exists()) {
			System.out.println(file.getName());
			file.delete();
		}
		
		bw2.flush();
		bw1.flush();
		bw2.close();
		br.close();
		bw1.close();
		
		
	}

}
