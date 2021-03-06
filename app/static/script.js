window.onload = () => {
	console.log("Life is pain!")
}

function folderclick(folder, currentFolder) {
	var filepath = `${currentFolder}/${folder}`
	fetch("https://134.122.121.84/set_cookie", {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({"filepath": filepath, "currentFolder": currentFolder})
	})
}

function folderback(lastfolder) {
	if (lastfolder == "/root/ftpfolder") {
		fetch("https://134.122.121.84/set_cookie", { // https://134.122.121.84
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({"filepath": lastfolder, "currentFolder": lastfolder})
		})
		return;
	}
	parentFolder = lastfolder.split('/')
	parentFolder.pop()
	lastfolder = lastfolder.replace('/', '/')
	parentFolder = parentFolder.join('/')
	fetch("https://134.122.121.84/set_cookie", {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({"filepath": lastfolder, "currentFolder": parentFolder})
	})
}
