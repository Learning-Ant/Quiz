package solved.baekjoon.step07;

import java.util.Scanner;

class Constant {

	private int[] constant; // 받은 값을 저장할 배열
	
	public Constant(int number) { // 받은 값을 배열에 역순으로 저장하는 생성자
		constant = new int[(int)(Math.log10(number))+1]; //로그를 이용해 자릿수 계산
		for(int i = 0;i<constant.length;i++) {
			constant[i]=number%10;
			number/=10;
		}
	}
	public int check(Constant constant) { // this와 인수로 받은 객체간의 정수크기 비교
		if(this.toInt()>constant.toInt()) {
			return this.toInt();
		} else {
			return constant.toInt();
		}
		
	}
	public int toInt() { // 배열을 이용해 정수로 만들어줌
		int temp=0;
		for(int i=0;i<constant.length;i++){
			temp+=constant[i]*Math.pow(10, constant.length-(i+1));
		}
		return temp;
	}
}



// 보다 쉽게 풀 수 있긴 하지만 class를 정의하여 사용하는 방법을 사용
public class Quiz2908 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Constant con1=new Constant(sc.nextInt());
		Constant con2=new Constant(sc.nextInt());
		
		System.out.println(con1.check(con2));
		sc.close();
	}

}
