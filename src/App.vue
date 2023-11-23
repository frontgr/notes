<script setup>
import { ref } from "vue";

const notes = ref([]);
const newNote = ref("");
newNote.value = "";
const addNote = () => {
  if (newNote.value) {
    notes.value.push(newNote.value);
    newNote.value = "";
  }
};
</script>

<template>
  <div class="container">
    <textarea v-model="newNote" placeholder="Enter a note"></textarea>
    <button @click="addNote">Add Note</button>
    <ul>
      <li v-for="note in notes" :key="note">{{ note }}</li>
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
  display: block;
  width: 100%;
  padding: 10px;
  background-color: #4caf50;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  margin-bottom: 5px;
}
</style>
