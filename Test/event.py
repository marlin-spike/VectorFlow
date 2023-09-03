from flask import Flask, request, Response
import time

app = Flask(__name__)

@app.route('/')
def index():
    return """
    <html>
        <head>
            <title>SSE Example</title>
        </head>
        <body>
            <h1>Server-Sent Events Example</h1>
            <div id="sse">
            </div>
            <script>
                var sse = new EventSource("/events");
                sse.onmessage = function(event) {
                    document.getElementById('sse').innerHTML += "<p>" + event.data + "</p>";
                };
            </script>
        </body>
    </html>
    """

# SSE route to listen for client connections
@app.route('/events')
def sse():
    def event_stream():
        try:
            while True:
                # Simulate some work
                time.sleep(1)
                
                # Detect client disconnection and handle it
                if request.environ.get('wsgi.websocket'):
                    print("Client disconnected")
                    break
                
                yield "Server Message\n"  # Send a message to the client
        except GeneratorExit:
            print("Generator closed")
    
    return Response(event_stream(), content_type='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True)
