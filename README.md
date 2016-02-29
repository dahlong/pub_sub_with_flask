# pub_sub_with_flask
A simple implementation of dynamic bar chart in a web page. 
Using a python app to audit a log file(test_json.log).
When a new line was added in the log file, the app publishs messages to a redis server.
The web app subscribes the messages from the redis and sends messages through server-sent event(SSE) to html page(redraw.html).
Then the html page visualizes the messages(json format) by dimple.js.
