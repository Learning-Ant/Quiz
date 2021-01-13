package solved.baekjoon.step01;

import java.io.IOException;
import java.util.Scanner;

public class Quiz10998 {

	public static void main(String[] args) throws IOException{

		// 두 정수 A와 B를 입력받은 다음, A×B를 출력하는 프로그램을 작성하시오.
		
		// Scanner 클래스로 읽어오고, println()메소드로 출력한다.
		// 12880KB 116ms
		
		// 확실히 BufferedReader 클래스와 BufferedWriter 클래스를 이용할 때보다
		// 큰 차이는 없지만 시간과 메모리 사용이 크다.
		Scanner sc = new Scanner(System.in);
		
		System.out.println(sc.nextInt()*sc.nextInt());
	
		sc.close();
	}

}
