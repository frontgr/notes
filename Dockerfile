FROM node:lts
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build
RUN npm install -g serve
CMD [ "serve", "-p", "4000", "dist" ]