package solved.baekjoon.step07;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Quiz11720 {

	public static void main(String[] args) throws IOException {

		// N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	    int length=Integer.parseInt(br.readLine());
	    if(length>100||length<1) return;
	    String strNumber=br.readLine();
	    int sum=0;
	    for (int i=0;i<strNumber.length();i++){
	    sum+=strNumber.charAt(i)-48;
	    }
	    System.out.println(sum);
	}

}
