package Ch1;

import java.util.Scanner;

// n이 7이면 '1+2+3+4+5+6+7=28'로 출력하는 프로그램을 작성하시오.
// 추가적으로 n이 꼭 7이 아니여도 위의 방식되로 출력되면 된다. n는 사용자한테 입력받는 값
public class Q7_Sum {
    public static void main(String[] args) {

        //for문 사용 시 주의사항
        /*
        1. for문의 초기화 부분, 제어식, 업데이트 부분은 생략 가능. 단, 세미콜론(;)은 생략하면 안 된다.
        2. for문의 초기화 부분에서 선언한 변수는 for문 안에서만 유효하다.
           for문을 종료한 다음에도 변수를 사용하려면 for문 밖에 변수를 선언해줘야 한다.
         */
        Scanner sc = new Scanner(System.in);

        int n;
        System.out.print("n의 값 : ");
        n = sc.nextInt();

        // 합을 구하는 식
        int sum = 0; // sum : 합

        // i는 1부터 n까지 반복(증감)
        for(int i=1; i<=n; i++) {
            //만약 i가 n보다 작으면
            if(i<n)
                // 1부터 n까지의 합을 구하기 때문에 i가 n보다 작으면  i값과 + 부호를 출력한다.
                System.out.print(i + " + ");
            // 그렇지 않으면(i가 n보다 작지 않으면)
            else
                // 이때는 i=n이 된 상황이기에 +부호는 생략하고 i만 출력한다
                System.out.print(i);
            // 반복(for문)하면서 sum에 i값을 누적한다(합계)
            sum += i; // sum에 i를 더함
        } //end for문

        // 계산이 끝났으므로 = 부호는 출력하면서 sum(합계를) 출력해준다.
        System.out.println(" = " + sum);

    }
}