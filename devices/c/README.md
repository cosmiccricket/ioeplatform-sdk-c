This is a C-implementation of the Internet of Things SDK.
========================================================

It includes several directories:
> apps : Standalone applications that you can use for reference source code
         to build and use your own agents.
         
> include : Global headers. Library headers are automatically copied in when
            you build the lib directory.
            
> iot : IOT stands for "Internet of Things". This directory contains tools
        your applications need to connect to the Internet and communicate.
        
> lib : Libraries. Make this directory and copy or symlink the .so's into 
        /usr/lib.  You may need to make the 3rd party libraries individually.
        
> support : Support files for the compile toolchain

The $IOTSDK environment variable can define where your iotsdk directory is
located. This environment variable may be used in your own applications'
Makefiles outside of this open source repository, and is sometimes
used in application Makefiles within this open source repository as well.



Here's how it works...
----------------------
PROXY
The iot/proxy directory is one of the main components of this SDK. It 
implements a persistent HTTP connection with a cloud server which allows 
clients to send data (which are buffered and pushed out periodically),
and receive commands almost instantaneously from a cloud server.

The proxy itself doesn't care about the data that is being passed back and
forth, but it does wrap the data in proper XML headers for communication
with the cloud.


PROXYSERVER APPLICATION
The apps/proxyserver application creates a proxy instance and opens a socket so 
multiple agents can all share the same proxy instance.  Users of the proxyserver
can use the clientsocket component found in iot/client to connect to the 
proxyserver's open socket.

You must activate your proxyserver using the command: proxyserver -a [key],
where the [key] is given to you by People Power Company to bind your
physical device with your username.


XML
The iot/xml directory contains an important file:  iotapi.h.

This header defines function prototypes you would use to create XML
to send to the server, or receive commands from the server.

The header is implemented in the iot/xml/parser and iot/xml/generator 
directories. You would normally compile in the parser and the generate
with your agent in order to automatically deal with the XML data from the
cloud servers.

EXAMPLEAGENT
The apps/exampleagent is a template for an agent that would connect to the
proxyserver's socket and manage a set of homogeneous devices.  It actually
does not function, but it compiles. 

