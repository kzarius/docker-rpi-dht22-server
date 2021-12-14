FROM arm32v6/node:alpine

WORKDIR /usr/src/app
RUN npm ci --production && npm clean cache --force

CMD ["npm","start"]