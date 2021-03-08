package unsolved.baekjoon;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.EmptyStackException;
import java.util.Stack;

public class Quiz10828 {
	
	private static Stack<Integer> stack;
	private static int size = 0;
	

	
	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int testCase = Integer.parseInt(br.readLine());
		stack = new Stack<Integer>();
		try {
			for(int i = 0;i < testCase;i++) {
				String[] command = br.readLine().split(" ");
				if(command.length<2) {
					switch(command[0]) {
					case "size" : bw.write(String.valueOf(size)); break;
					case "pop" : bw.write(String.valueOf(stack.pop()));
								size--;
								break;
					case "empty" : bw.write(stack.isEmpty()?"1":"0"); break;
					// case "top" : bw.
					}
				} else {
					stack.push(Integer.parseInt(command[1]));
				}
				bw.write("\n");
			}
		} catch(EmptyStackException e) {
			bw.write("1");
		}
		
		bw.flush();
		bw.close();
		br.close();
	}

}
