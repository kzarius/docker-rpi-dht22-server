FROM arm32v6/node:alpine

WORKDIR /usr/src/app

# Install the dependencies.
COPY package*.json ./
RUN npm ci --only=production

COPY . .

CMD ["node","server.js"]