FROM node:18-alpine

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

# Exponemos el puerto de desarrollo de Vite/React
EXPOSE 5173

CMD ["npm", "run", "dev", "--", "--host"]