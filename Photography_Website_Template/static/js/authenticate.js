//confirm password
var submit = document.getElementById('submit')
var check = function() {
    if (document.getElementById('password').value ==
        document.getElementById('confirm-password').value) {
        document.getElementById('message').style.color = 'green';
        document.getElementById('message').style.fontSize = '0.8em';
        document.getElementById('message').innerHTML = 'matching';
        submit.disabled = false
    } else {
        document.getElementById('message').style.color = 'red';
        document.getElementById('message').style.fontSize = '0.8em';
        document.getElementById('message').innerHTML = 'not matching';
        submit.disabled = true
    }
}