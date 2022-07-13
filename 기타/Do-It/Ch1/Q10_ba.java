package Ch1;

import java.util.Scanner;

// 두 변수 a,b에 정수를 입력하고 b - a 를 출력하는 프로그램을 작성하시오.
// 단, a가 b보다 크거나 같으면 b를 다시 입력하도록 작성
public class Q10_ba {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        
        int a;

        System.out.print("a의 값 : ");
        a = sc.nextInt();

        int b = 0;
        while(true) {
            System.out.print("b의 값 : ");
            b = sc.nextInt();
            if(b>a)
                break;
            System.out.println("a보다 큰 값을 입력하세요!");
        }
        System.out.println("입력된 b값 : " + b + ", 입력된 a값 : " + a);
        System.out.println("b-a는 " + (b-a) + " 입니다.");


            
        
    }
}
