I will supply some websites and documentation to get familiar with, may be helpful
to refer back to this page if you decide to implement these functions. Some of these
are popular python libraries, so it wouldn't hurt to get familiar with them.


os.py:

    Some functions from this module:
        os.listdir(): Lists all files and directories in a specified path.
        os.mkdir(): Creates a directory.
        os.makedirs(): Creates directories recursively; it creates all the intermediate-level folders needed to contain the leaf directory.
        os.remove(): Removes a file.
        os.rmdir(): Removes a directory.
        os.rename(): Renames a file or directory.
        os.path.join(): Joins one or more path components intelligently.
        os.path.split(): Splits a path into its directory and file name components.
        os.path.exists(): Checks if a path exists.
        os.path.isdir(): Checks if a specified path is a directory.
        os.path.isfile(): Checks if a specified path is a file.
        os.getcwd(): Gets the current working directory.
        os.chdir(): Changes the current working directory.



    Docs: https://docs.python.org/3/library/os.html



socket.py:

    Some functions from this module:
        socket.socket(): Creates a new socket, which is the endpoint for sending and receiving data.
        socket.bind((host, port)): Binds the socket to an address (host, port).
        socket.listen(backlog): Enables a server socket to accept connections, with backlog specifying the number of unaccepted connections that the system will allow before refusing new connections.
        socket.accept(): Accepts a connection request from a client socket. It returns a pair (conn, address) where conn is a new socket object usable to send and receive data on the connection, and address is the address bound to the socket on the other end of the connection.
        socket.connect((host, port)): Initiates a connection to a remote socket at the specified host and port.
        socket.send(bytes): Sends data from the socket. The maximum amount of data to be sent at once is specified by bytes.
        socket.recv(bufsize): Receives data from the socket, with bufsize specifying the maximum amount of data to be received at once.
        socket.close(): Closes the socket, immediately freeing the resource associated with it.


    Docs: https://docs.python.org/3/library/socket.html#module-socket

