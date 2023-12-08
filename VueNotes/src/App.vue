<script setup>
import { ref, onMounted } from "vue";

const notes = ref([]);
const newNote = ref("");
newNote.value = "";
const addNote = async () => {
  if (newNote.value) {
    const note = { content: newNote.value };
    try {
      const response = await fetch("http://localhost:8085/add-note", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(note),
      });
      if (response.ok) {
        notes.value.push(newNote.value);
        newNote.value = "";
      } else {
        console.error("Failed to add note");
      }
    } catch (error) {
      console.error(error);
    }
  }
};
const deleteNotes = async () => {
  try {
    const response = await fetch("http://localhost:8085/clear-all", {
      method: "DELETE",
    });
    notes.value = [];
    newNote.value = "";
  } catch (error) {
    console.error(error);
  }
};
onMounted(async () => {
  try {
    const response = await fetch("http://localhost:8085/get-notes");
    const data = await response.json();
    notes.value = data.map((item) => item.content);
  } catch (error) {
    console.error(error);
  }
});
</script>

<template>
  <div class="container">
    <textarea v-model="newNote" placeholder="Enter a note"></textarea>
    <div class="btn-container">
      <button @click="addNote">Add Note</button>
      <button @click="deleteNotes">Delete Notes</button>
    </div>
    <ul>
      <li v-for="note in notes" :key="note" class="note-item">{{ note }}</li>
    </ul>
  </div>
</template>

<style scoped>
.container {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f5f5f5;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.btn-container {
  display: flex;
  justify-content: space-between;
  margin-bottom: 10px;
  gap: 10px;
}

textarea {
  width: calc(100% - 10px);
  height: 90px;
  padding: 5px;
  margin-bottom: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 16px;
}

button {
  display: inline-block;
  width: 100%;
  padding: 10px;
  background-color: #87af4c;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
button:nth-child(2) {
  background-color: #af5b4c;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  margin-bottom: 5px;
  background-color: #fff;
  padding: 10px;
  border-radius: 4px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  margin-bottom: 5px;
}
</style>
