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
  <div>
    <textarea v-model="newNote" placeholder="Enter a note"></textarea>
    <button @click="addNote">Add Note</button>
    <ul>
      <li v-for="note in notes" :key="note">{{ note }}</li>
    </ul>
  </div>
</template>

<style scoped></style>
