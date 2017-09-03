
  $('#search').click(function() {
        a=$("#searchString").val();
	$('#question')[0].innerText=a+"?"
        document.getElementsByClassName("font-weight-normal")[0].innerText="typing..."
	var obj ="{\"yourname\" : \""+a+"\"}"
	var settings = {
	  "async": true,
	  "crossDomain": true,
	  "url": "http://localhost:5000/test",
	  "method": "POST",
	  "headers": {
	    "content-type": "application/json",
	    "cache-control": "no-cache"
	  },
	  "processData": false,
	  "data": obj
	}

	$.ajax(settings).done(function (response) {
	  console.log(response);
          $('#reply')[0].innerText=response
          document.getElementsByClassName("font-weight-normal")[0].innerText="Online"
	});
       
    });

