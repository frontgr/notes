FROM node:lts
RUN mkdir app
WORKDIR /app
COPY ../package.json /app
RUN npm install
COPY ../VueNotes /app
RUN npm run build
RUN npm install -g serve

CMD [ "serve", "-p", "4000", "dist" ]