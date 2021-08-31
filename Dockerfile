FROM nginx:1.21.1-alpine
COPY data/etc/nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf
ENTRYPOINT ["/docker-entrypoint.sh"]
EXPOSE 80
STOPSIGNAL SIGQUIT
CMD ["/usr/sbin/nginx", "-g", "daemon off;"]
