ARG BASE_IMAGE=node:18.7-alpine 
FROM ${BASE_IMAGE} as packages-installed

WORKDIR /app

COPY angular.json .browserslistrc package-lock.json package.json tsconfig.json tsconfig.app.json tailwind.config.js /app/

RUN npm ci 

FROM packages-installed as builder
COPY src/ /app/src
RUN npm run build

FROM packages-installed as dev
COPY src/ app/src
CMD npm start -- --host 0.0.0.0 --port 4200 

FROM nginx:1.23.0-alpine
EXPOSE 8080
COPY nginx.conf /etc/nginx/nginx.conf
COPY --from=builder /app/dist/frontend /usr/share/nginx/html
