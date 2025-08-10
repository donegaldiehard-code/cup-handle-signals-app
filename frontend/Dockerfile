FROM node:18-alpine
WORKDIR /app
COPY . /app
RUN npm install
RUN npm run build
EXPOSE 80
RUN npm install -g serve
CMD ["serve", "-s", "build"]