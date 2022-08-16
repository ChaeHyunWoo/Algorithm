package com.programmers.java;

class 콜라츠추측 {
    public int solution(int num) {

        // 마지막 테스트 케이스 626331 * 3 +1 범위 때문에 int는 안됨 -> long으로
        long n = (long)num;

        // 작업을 500번 반복할 때까지 1이 되지않으면 -1 반환 -> i<500
        for(int i=0; i<500; i++) {
            // 1을 입력받으면 0 반환
            if(n == 1)
                return i;
            // 공식
            n = (n%2 == 0) ? n/2 : n*3+1;
        }
        return -1;

    }
}