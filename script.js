// ==================== Tab Switching ====================
const tabs = document.querySelectorAll('.tab');
const taskLists = document.querySelectorAll('.task-list');

tabs.forEach(tab => {
  tab.addEventListener('click', () => {
    tabs.forEach(t => t.classList.remove('active'));
    tab.classList.add('active');

    const day = tab.getAttribute('data-day');
    taskLists.forEach(list => list.classList.remove('active'));
    document.getElementById(day).classList.add('active');

    updateProgress(day);
    highlightCurrentTask(day);
  });
});

// ==================== Progress Bar ====================
function updateProgress(dayId) {
  const list = document.getElementById(dayId);
  const tasks = list.querySelectorAll('input[type="checkbox"]');
  const total = tasks.length;
  const done = Array.from(tasks).filter(t => t.checked).length;
  const percent = Math.round((done / total) * 100);

  document.getElementById('progress').style.width = percent + '%';
  document.getElementById('progress-text').textContent = percent + '% selesai';
}

// ==================== Checkbox Event & LocalStorage ====================
function saveTasks(dayId) {
  const list = document.getElementById(dayId);
  const tasks = list.querySelectorAll('input[type="checkbox"]');
  const state = Array.from(tasks).map(t => t.checked);
  localStorage.setItem(dayId, JSON.stringify(state));
}

function loadTasks(dayId) {
  const list = document.getElementById(dayId);
  const tasks = list.querySelectorAll('input[type="checkbox"]');
  const saved = JSON.parse(localStorage.getItem(dayId)) || [];
  tasks.forEach((task, i) => {
    task.checked = saved[i] || false;
    task.parentElement.classList.toggle('done', task.checked);
  });
}

taskLists.forEach(list => {
  const dayId = list.id;
  const tasks = list.querySelectorAll('input[type="checkbox"]');

  // Load saved state
  loadTasks(dayId);

  // Add event
  tasks.forEach(task => {
    task.addEventListener('change', () => {
      task.parentElement.classList.toggle('done', task.checked);
      updateProgress(dayId);
      saveTasks(dayId);
    });
  });
});

// ==================== Highlight Current Task ====================
function highlightCurrentTask(dayId) {
  const list = document.getElementById(dayId);
  const now = new Date();
  const currentMinutes = now.getHours() * 60 + now.getMinutes();

  list.querySelectorAll('.task').forEach(task => {
    task.style.borderColor = '#c0a060'; // default border
    const text = task.querySelector('span').textContent;
    const match = text.match(/(\d{2}):(\d{2}) - (\d{2}):(\d{2})/);
    if (match) {
      const startMinutes = parseInt(match[1]) * 60 + parseInt(match[2]);
      const endMinutes = parseInt(match[3]) * 60 + parseInt(match[4]);
      if (currentMinutes >= startMinutes && currentMinutes <= endMinutes) {
        task.style.borderColor = '#FFD700'; // gold highlight
      }
    }
  });
}

// ==================== Drag & Drop ====================
let draggedItem = null;

taskLists.forEach(list => {
  const tasks = list.querySelectorAll('.task');
  tasks.forEach(task => {
    task.addEventListener('dragstart', () => {
      draggedItem = task;
      setTimeout(() => task.classList.add('dragging'), 0);
    });

    task.addEventListener('dragend', () => {
      draggedItem = null;
      task.classList.remove('dragging');
      saveTasks(list.id); // save urutan baru
    });

    task.addEventListener('dragover', e => {
      e.preventDefault();
      const draggingOverItem = task;
      if (draggingOverItem !== draggedItem) {
        const parent = draggingOverItem.parentNode;
        const bounding = draggingOverItem.getBoundingClientRect();
        const offset = e.clientY - bounding.top;
        if (offset > bounding.height / 2) {
          parent.insertBefore(draggedItem, draggingOverItem.nextSibling);
        } else {
          parent.insertBefore(draggedItem, draggingOverItem);
        }
      }
    });
  });
});

// ==================== Auto Highlight Update ====================
setInterval(() => {
  const activeList = document.querySelector('.task-list.active');
  highlightCurrentTask(activeList.id);
}, 60000); // update tiap 1 menit

// ==================== Inisialisasi ====================
document.addEventListener('DOMContentLoaded', () => {
  const activeList = document.querySelector('.task-list.active');
  updateProgress(activeList.id);
  highlightCurrentTask(activeList.id);
});
