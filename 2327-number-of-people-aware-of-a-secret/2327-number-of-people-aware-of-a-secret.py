class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        Mod = 10 ** 9 + 7
        #비밀을 알고 있는 사람들의 수를 저장, secret[n]은 n번째 날에 비밀을 알고 있는 사람 수
        secret = [0] * (n + 1)
        secret[1] = 1   #첫째 날에는 한 사람만 아므로 1로 설정

        for days in range(2, n+1) :
            #delay ~ forget일까지 
            for forget_time in range(delay, forget) : 
                if days - forget_time >= 1 :
                    secret[days] = (secret[days] + secret[days - forget_time]) % Mod

        
        #n + 1 - forget 일 부터 n까지의 날짜 : 비밀을 잊지 않은 사람
        return sum(secret[n + 1 - forget:]) % Mod