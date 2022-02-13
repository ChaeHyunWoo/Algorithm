package fastcampus_java;

public class MinMaxNumber {

    public static void main(String[] args) {

        int [] numbers = {10,55,23,2,79,101,16,82,30,45};

        int min = numbers[0];
        int max = numbers[0];

        int minPos = 0;
        int maxPos = 0;

        //배열의 길이만큼 반복문을 돌린다.
        for(int i=1; i< numbers.length; i++) {

            if(min > numbers[i]) {
                min = numbers[i];
                minPos = i+1;
            }

            if(max < numbers[i]) {
                max = numbers[i];
                maxPos = i;
            }
        }
        System.out.println("가장 큰 값 : " + max + " 위치는 " + maxPos + "번 째");
        System.out.println("가장 작은 값 : " + min + " 위치는 " + minPos + "번 째");
    }
}
