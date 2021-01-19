package solved.baekjoon.step06;

public class Quiz15596 {

	/*
	 * Java: long sum(int[] a); (클래스 이름: Test) a: 합을 구해야 하는 정수 n개가 저장되어 있는 배열 (0 ≤
	 * a[i] ≤ 1,000,000, 1 ≤ n ≤ 3,000,000) 리턴값: a에 포함되어 있는 정수 n개의 합
	 */
	
	public long sum(int[] a) {
		long sum=0;
		
		// 422800KB	28ms
		for(int i=0, size=a.length;i<size;i++) {
			sum+=a[i];
		}
		
		// 422800KB	24ms
		for(int i=0;i<a.length;i++){
            sum += a[i];
        }
		
		return sum;
	}
}
