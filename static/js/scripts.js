document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll("form").forEach(form => {
        form.addEventListener("submit", function () {
            let saveButton = form.querySelector(".save-btn");
            if (saveButton) {
                saveButton.disabled = true;
                saveButton.querySelector(".spinner-border").classList.remove("d-none");
                saveButton.innerHTML = `<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Saving...`;
            }
            console.log("[UI] Form submitted for project:", form.action);
        });
    });

    console.log("[UI] Page loaded. Ready for user interaction.");
});

// Capture console logs and display in UI
(function () {
    let oldConsoleLog = console.log;
    console.log = function (...args) {
        oldConsoleLog.apply(console, args);  // Keep original console.log functionality

        let logContent = document.getElementById("logContent");
        if (!logContent) return;

        let logEntry = document.createElement("div");

        // Convert objects to JSON strings for better display
        let formattedMessage = args.map(arg => (typeof arg === "object" ? JSON.stringify(arg, null, 2) : arg)).join(" ");

        logEntry.textContent = "> " + formattedMessage;
        logContent.appendChild(logEntry);
        logContent.scrollTop = logContent.scrollHeight; // Auto-scroll to the latest log
    };
})();

// Toggle the log panel when the button is clicked
document.getElementById("showLogsButton").addEventListener("click", function () {
    let logPanel = document.getElementById("logPanel");
    logPanel.style.display = logPanel.style.display === "none" ? "block" : "none";
    console.log("[Logging] Toggled log panel: " + (logPanel.style.display === "block" ? "Opened" : "Closed"));
});

// Logging of macro calls within HTML
function logMacro(category, label, value) {
    let formattedValue = (typeof value === "object") ? JSON.stringify(value, null, 2) : value;
    console.log(`[${category}] ${label} → Selected: ${formattedValue}`);
}

// Log Dropdown Selections
function logDropdownSelection(name, value) {
    logMacro("Dropdown", name, value || "None");
}

// Log Multi-Select Selections
function logMultiSelectCall(selectName) {
    let selectElement = document.querySelector(`select[name="${selectName}[]"]`);
    if (!selectElement) {
        console.error(`Multi-select '${selectName}' not found.`);
        return;
    }
    let selectedOptions = Array.from(selectElement.selectedOptions).map(option => option.text);
    logMacro("Multi-Select", selectName, selectedOptions);
}

// Clear logs from the panel
function clearLogs() {
    document.getElementById("logContent").innerHTML = "";
}

// Prevent row click from triggering when clicking direct actions (e.g., Delete)
document.querySelectorAll('.btn').forEach(button => {
    button.addEventListener('click', (e) => {
        e.stopPropagation();
    });
});

// Trigger filter logic whenever a filter input changes
document.querySelectorAll('.column-filter').forEach(input => {
    input.addEventListener('input', function () {
        console.log("[Filtering] Column:", this.getAttribute('data-column'), "Value:", this.value);
        filterTable();
    });
});

function filterTable() {
    const filters = {};
    document.querySelectorAll('.column-filter').forEach(input => {
        filters[input.getAttribute('data-column')] = input.value.toLowerCase();
    });
    document.querySelectorAll('tr.main-row').forEach(row => {
        const cells = row.querySelectorAll('td');
        let show = Object.keys(filters).every(colIndex => {
            const filterVal = filters[colIndex];
            const cellText = cells[colIndex].textContent.trim().toLowerCase();
            if (filterVal === "" && cellText === "-") {
                return false;
            }
            return filterVal === "" || cellText.includes(filterVal);
        });
        row.style.display = show ? "" : "none";
    });

    console.log("[Filtering] Applied:", filters);
}

// Sorting functionality with logging
const sortDirections = {};
function sortTableByColumn(colIndex, clickedHeader) {
    let rows = Array.from(document.querySelectorAll('tbody tr.main-row'));
    console.log("[Sorting] By column:", colIndex);

    if (colIndex === 0) {
        rows.sort((a, b) => {
            const aVal = parseInt(a.cells[colIndex].textContent);
            const bVal = parseInt(b.cells[colIndex].textContent);
            return sortDirections[colIndex] === "asc" ? aVal - bVal : bVal - aVal;
        });
    } else if (colIndex === 3) {
        rows.sort((a, b) => {
            const aDate = new Date(a.cells[colIndex].textContent);
            const bDate = new Date(b.cells[colIndex].textContent);
            return sortDirections[colIndex] === "asc" ? aDate - bDate : bDate - aDate;
        });
    }

    sortDirections[colIndex] = sortDirections[colIndex] === "asc" ? "desc" : "asc";
    const tbody = document.querySelector('tbody');
    tbody.innerHTML = "";
    rows.forEach(row => tbody.appendChild(row));

    console.log("[Sorting] Direction:", sortDirections[colIndex]);
}

document.querySelectorAll("#headerRow th.sortable").forEach((th, index) => {
    th.addEventListener("click", function () {
        sortTableByColumn(index, th);
    });
});

function toggleCameraImage(cameraId) {
    var checkbox = document.getElementById("camera_" + cameraId);
    var container = document.getElementById("camera_" + cameraId + "_container");

    if (!checkbox || !container) {
        console.error("[Error] Missing camera elements for ID:", cameraId);
        return;
    }

    checkbox.checked = !checkbox.checked;
    if (checkbox.checked) {
        container.classList.add("disabled");
    } else {
        container.classList.remove("disabled");
    }

    console.log(`[Location] Camera ${cameraId} toggled. Checked: ${checkbox.checked}`);
}

function toggleSeat(seatId, projectId) {
    let checkbox = document.getElementById(`${seatId}_${projectId}`);
    let image = document.getElementById(`seat_img_${seatId}_${projectId}`);

    if (!checkbox || !image) {
        console.error(`[Error] Element not found for seatId: ${seatId}, projectId: ${projectId}`);
        return;
    }

    checkbox.checked = !checkbox.checked;
    image.style.visibility = checkbox.checked ? "visible" : "hidden";

    console.log(`[Seating] Seat ${seatId} toggled. Checked: ${checkbox.checked}`);
}

document.addEventListener("DOMContentLoaded", function () {
    filterTable();
    Array.from(document.querySelectorAll('.toast')).forEach(toastEl => {
        const toast = new bootstrap.Toast(toastEl, { delay: 3000 });
        toast.show();
    });

    console.log("[Filtering] Initial table filtering applied.");
});
