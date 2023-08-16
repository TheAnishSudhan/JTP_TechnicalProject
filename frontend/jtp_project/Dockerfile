FROM node:lts-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
# ENV PORT=8080
EXPOSE 5173
# CMD [ "npm", "run", "dev" ]
CMD [ "npm", "run", "dev", "--", "--host", "0.0.0.0" ]