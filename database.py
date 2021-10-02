from motor import motor_asyncio
client = motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')
# client = motor.motor_asyncio.

db = client['test_database']
collection = db['test_collection']

async def do_insert():
    document = {'key': 'value'}
    result = await db.test_collection.insert_one(document)
    print('result %s' % repr(result.inserted_id))

import asyncio
loop = asyncio.get_event_loop()
loop.run_until_complete(do_insert())

#update 
async def do_replace(id):
    coll = db.test_collection
    old_document = await coll.find_one({'id': id})
    print('found document: %s' % print.pformat(old_document))
    _id = old_document['_id']
    result = await coll.replace_one({'_id': id}, {'key': 'value'})
    print('replaced %s document' % result.modified_count)
    new_document = await coll.find_one({'_id': _id})
    print('document is now %s' % print.pformat(new_document))

#DELETE
async def do_delete_many(id):
    coll = db.test_collection
    n = await coll.count_documents({})
    print('%s documents before calling delete_many()' % n)
    result = await db.test_collection.delete_many({'i': id})
    print('%s documents after' % (await coll.count_documents({})))
