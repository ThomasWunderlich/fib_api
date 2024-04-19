## Fibonacci API

This is a FastAPI app for getting the next item in the Fibonacci sequence.

- Endpoint: `/fib/{num}`
- Input: `num` must be an integer
- Output: The next integer in the Fibonacci sequence or "not a Fibonacci number."
- This will be returned as text _NOT_ as json per the instructions.

### Running in dev mode
1. Install dependencies by running `pip install requirements.txt`
2. Start the server via `uvicorn app.main:app --reload`
3. Requests can then be made to `http://127.0.0.1:8000/fib/{num}`

### Containerization
- Build the container via: `docker build -t container_name .`
- Run the container via: `docker run -d --name mycontainer -p 80:80 container_name`
- Requests can then be made to `http://127.0.0.1:80/fib/{num}`. If you're running this on a server, replace 127.0.0.1 with the host.
