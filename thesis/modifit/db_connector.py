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

def getAllItemData():
  try:
      conn = psycopg2.connect("dbname='d5914cigeuchlr' user='rvcgzocqxdmppm' host='ec2-54-204-7-145.compute-1.amazonaws.com' password='b-wim0PggajRFhcwO_NiEnjvtW'")
  except:
      print "Can't connect to the database"

  cur = conn.cursor()
  try:
      query = "SELECT item_id, ARRAY_AGG(attribute_type), ARRAY_AGG(attribute_id) " \
            + "FROM modifit_hasattribute " \
            + "GROUP BY item_id ORDER BY item_id"
      cur.execute(query)
  except:
      print "Can't execute query"

  items = {}
  rows = cur.fetchall()
  for row in rows:
      attribute = {}
      #print row[0]
      for i in range(len(row[1])):
          attribute[row[1][i]] = row[2][i]
          #print row[1][i] + ": " + str(row[2][i]) # attribute type: attribute
      items[row[0]] = attribute

  #print items
  return items
      #output items
      #put users in jaccard index

def getCategoryItemData(category):
  try:
      conn = psycopg2.connect("dbname='d5914cigeuchlr' user='rvcgzocqxdmppm' host='ec2-54-204-7-145.compute-1.amazonaws.com' password='b-wim0PggajRFhcwO_NiEnjvtW'")
  except:
      print "Can't connect to the database"

  cur = conn.cursor()
  try:
      query = "SELECT ha.item_id, ARRAY_AGG(attribute_type), ARRAY_AGG(attribute_id) " \
            + "FROM modifit_hasattribute AS ha, modifit_hascategory AS hc " \
            + "WHERE ha.item_id = hc.item_id AND category_id = " + category + " " \
            + "GROUP BY ha.item_id ORDER BY ha.item_id"
      cur.execute(query)
  except:
      print "Can't execute query"

  items = {}
  rows = cur.fetchall()
  for row in rows:
      attribute = []
      #print row[0]
      for i in range(len(row[1])):
          attribute.append((row[1][i], row[2][i]))
          #print row[1][i] + ": " + str(row[2][i]) # attribute type: attribute
      items[row[0]] = attribute

  #print items
  return items
      #output items
      #put users in jaccard index