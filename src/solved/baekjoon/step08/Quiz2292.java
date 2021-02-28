package solved.baekjoon.step08;

import java.util.Scanner;

public class Quiz2292 {

	public static int recurrence(int n) {
		return 3*n*n-3*n+1; // 벌집 점화식
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int goal = sc.nextInt();
		int count = 1;
		while(true) {
			if(goal==1) {
				break;
			}
			else if(recurrence(count)<goal && recurrence(count+1)>=goal){
				break;
			}
			count++;
		}
		System.out.println(goal==1?count:++count);
		sc.close();
	}

}
