function downloadReport() {
    window.location.href = "/download-report";
}

window.onload = () => {
    fetch("/get-audit-logs")
        .then(res => res.json())
        .then(data => {
            const list = document.getElementById("logList");
            list.innerHTML = "";
            data.forEach(log => {
                let li = document.createElement("li");
                li.innerText = `[${log.time}] ${log.action}`;
                list.appendChild(li);
            });
        });
};
