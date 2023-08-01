FROM node:20
WORKDIR /app
COPY jtp_project ./
RUN npm install
COPY . .
ENV PORT=8080
EXPOSE 5173
CMD [ "npm", "start" ]