import psycopg2

def getAllWardrobeData():
  try:
      conn = psycopg2.connect("dbname='d5914cigeuchlr' user='rvcgzocqxdmppm' host='ec2-54-204-7-145.compute-1.amazonaws.com' password='b-wim0PggajRFhcwO_NiEnjvtW'")
  except:
      print "Can't connect to the database"

  cur = conn.cursor()
  try:
      query = "SELECT user_id, ARRAY_AGG(item_id), ARRAY_AGG(rating) " \
            + "FROM modifit_wardrobe " \
            + "GROUP BY user_id ORDER BY user_id"
      cur.execute(query)
  except:
      print "Can't execute query"

  users = {}
  rows = cur.fetchall()
  for row in rows:
      wardrobe = {}
      #print row[0] # user
      for i in range(len(row[1])):
          wardrobe[row[1][i]] = row[2][i]
          #print row[1][i] + ": " + str(row[2][i]) # item: times used
      users[row[0]] = wardrobe

  return users
      #output users
      #put users in cosine similarity