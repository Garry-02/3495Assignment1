db = db.getSiblingDB("grades_db");

db.createCollection('sample_collection');

db.sample_collection.insertMany([
 {
    name: 'steven',
    set: 'b',
    term: '4'
  }
]);

