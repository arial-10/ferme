function toggleMenu() {
	var x = document.getElementById("menu");
	
	for (var i = x.children.length - 1; i >= 0; i--) {
		if (x.children[i].className === "nav-item") {
			x.children[i].className += " responsive";
		} else {
			if (x.children[i].className === "nav-item responsive") {
				x.children[i].className = "nav-item";
			}
		}
	}
}
