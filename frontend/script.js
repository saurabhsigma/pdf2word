document.getElementById('upload-form').addEventListener('submit', function(event) {
    event.preventDefault();

    let formData = new FormData();
    formData.append('file', document.getElementById('pdf-file').files[0]);

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.blob();
    })
    .then(blob => {
        let url = window.URL.createObjectURL(blob);
        let a = document.createElement('a');
        a.href = url;
        a.download = 'output.docx';
        document.getElementById('download-link').href = url;
        document.getElementById('download-link').style.display = 'inline';
        a.click();
    })
    .catch(error => console.error('There was a problem with the fetch operation:', error));
});
