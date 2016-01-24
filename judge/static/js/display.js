function deps() {
	var str = 
	' <head> ' +
	' 	<link id="hdep0" rel="stylesheet" type="text/css" href="/static/css/bootstrap.min.css" media="screen"> ' +
	' </head>' +
	' <body> ' +
	'   <script id="hdep1" src="/static/js/bootstrap.min.js"></script> ' +
	'   <script id="hdep2" src="/static/js/display.js"></script> ' +
	'   <script id="hdep3" src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script> ' +
	'   <script id="hdep4" src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script> ' +
	' </body> ';
	return str;
}

function appendById(d, id) {
	var cluster = document.getElementById(id);
	var content = cluster.innerHTML;
	
	d.write( content );
}

function display(id) {
	var w = window.open();
	var d = w.document;
	
	d.open();
	
	d.write(deps());
	appendById(d, id);
	
	d.close();
} 
