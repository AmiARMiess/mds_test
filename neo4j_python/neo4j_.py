from neo4j import GraphDatabase
from uuid import uuid4
import pandas as pd

# The following class is based on the "Create a graph database in Neo4j using Python" 
# tutorial by CJ Sullivan, Feb 10, 2021. 
# https://towardsdatascience.com/create-a-graph-database-in-neo4j-using-python-4172d40f89c4


class Neo4jConnection:
    
    def __init__(self, uri, user, pwd):
        self.__uri = uri
        self.__user = user
        self.__pwd = pwd
        self.__driver = None
        try:
            self.__driver = GraphDatabase.driver(self.__uri, auth=(self.__user, self.__pwd))
        except Exception as e:
            print("Failed to create the driver:", e)
        
    def close(self):
        if self.__driver is not None:
            self.__driver.close()

    def verify_connectivity(self):
        if self.__driver is None:
            raise RuntimeError("Driver not initialized!")
        self.__driver.verify_connectivity()
        
    def query(self, query, parameters=None, db=None):
        if self.__driver is None:
            raise RuntimeError("Driver not initialized!")
        with self.__driver.session(database=db) as session:
            response = list(session.run(query, parameters))
        return response
    
    def query_to_dataframe(self, query, parameters=None, db=None):
        df = pd.DataFrame([dict(_) for _ in self.query(query, parameters, db)])
        return df


if __name__ == "__main__":
    conn = Neo4jConnection(
        uri="bolt://localhost:7687",
        user="neo4j",
        pwd="<password_here>",
    )

    # try:
    #     conn.verify_connectivity()
    #     print("Connection established successfully.")

    # except Exception as e:
    #     print("Neo4j operation failed:", e)


# for i in range(0, 10):
    # qry = "CREATE (f:Flight) SET f.flight_id = '" + str(uuid4()) + "' RETURN f;"
    #print(qry)
    # result = conn.query(qry)
    #print(result)

# qry = "MATCH (f:Flight) RETURN f.flight_id;"
# result = conn.query(qry)
# print(result)


# for node in result:
#     print(node[0])

# df = conn.query_to_dataframe(qry)

# df = pd.read_csv('flights.csv')

# print(df.head())


# for airport in set(list(df['origin'].unique()) + list(df['dest'].unique())):
#     qry = "CREATE (a:Airport {id: '" + airport + "'}) RETURN a;"
#     print(qry)
#     conn.query(qry)


# for idx, row in df.iterrows():
#     qry = "MATCH (a1:Airport),(a2:Airport) WHERE a1.id = '" + row['origin'] + "' "
#     qry += " AND a2.id = '" + row['dest'] + "' "
#     qry += " CREATE (a1)-[f1:FLIES_TO]->(a2) "
#     qry += " CREATE (a1)<-[f2:FLIES_TO]-(a2) "
#     qry += " RETURN a1, a2, f1, f2;"
#     #print(qry)
#     conn.query(qry)

# qry = "MATCH (a:Airport) RETURN a.id;"
# data = conn.query_to_dataframe(qry)
# print(data)