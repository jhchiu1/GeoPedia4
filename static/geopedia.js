//javascript file

function geopediabookmark()
{
//use h1 tag to get location
	var h = document.querySelector("h1");
	var i = h.attributes["data-location"].value;

	geopediabookmarks();
//search location history stored in localStorage
	var g = JSON.parse(localStorage.geopedia);
	g.geopedia.history[i] = document.location;
	localStorage.geopedia = JSON.stringify(g);

	renderbookmarks();
};
//create list of bookmarks
function geopediabookmarks() {
	if(!localStorage.geopedia) {
		localStorage.geopedia=JSON.stringify(
			{
				geopedia: {
					history: {}
				}
			});
	}

    var bms = [];
	var h = JSON.parse(localStorage.geopedia).geopedia.history;
	for (i in h) { 
		if (!h.hasOwnProperty(i)) {
			continue;
		}

		bms.push([i, h[i]]);
	}

	return bms;
};

function renderbookmarks() {
	var bs = geopediabookmarks();

	if (bs.length == 0) {
		return;
	}

	var bms = document.getElementById("history");
//create unordered list of bookmarked search locations
	if (!bms) return;
	var bml = document.createElement("ul");
		
	for (var i = 0; i < bs.length; i++) {
		var bm = bs[i];
		var bme = document.createElement("li");
		var ba = document.createElement("a");
		var hra = document.createAttribute("href");
		hra.value = bm[1].href;
		ba.attributes.setNamedItem(hra);
		ba.textContent = bm[0];
		bme.appendChild(ba);
		bml.appendChild(bme);
	}

	bms.appendChild(bml);
};

renderbookmarks();
