function Logout() {
	sessionStorage.removeItem("file_currentuser")
	window.location.href = "../login"
}

$("#colled_rightuser").click(function () {
	console.log('e')
	window.location.href = "/usercenter"
	return false
})