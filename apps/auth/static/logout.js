window.addEventListener("beforeunload", function(event) {
    // 서버에 로그아웃 요청을 보냅니다.
    fetch('/logout', {
        method: 'POST', // 로그아웃 요청은 POST 메서드를 사용합니다.
        credentials: 'same-origin' // 현재 사용자의 인증 정보를 전송합니다.
    });
});
