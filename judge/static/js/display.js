function hello() {
	var w = window.open();
	var d = w.document;
	d.open();
	d.write("<p>Hello World</p>");
	d.close();
} 
