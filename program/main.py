from func_connections import connect_dydx

if __name__ == "__main__":
 
 #connect to client
 try:
    client = connect_dydx()
 except Exception as e:
    print(e)
    print("error connecting to client;", e)
    exit(1)
