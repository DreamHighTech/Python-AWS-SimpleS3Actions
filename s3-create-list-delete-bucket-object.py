import boto
import time

s3conn = boto.connect_s3() # 's3conn' is a variable and can be any name

# First let us print the current list of buckets.
print "====================================================="
print "The current list of buckets are:"
print "====================================================="
for bucket in s3conn.get_all_buckets():
        print "{name}\t\t{created}".format(
                name = bucket.name,
                created = bucket.creation_date,
        )
        
# Create a new bucket. FYI: Buckets names must be globally unique name
newbucket = s3conn.create_bucket('s3-demo-%s' % int(time.time()))

# Display the name of the newly created bucket
print "====================================================="
print "The newly created bucket is : " + newbucket.name
print "====================================================="

# Create a new key/value pair in the bucket.
newkey = newbucket.new_key('myobject')
newkey.set_contents_from_string("Hello World!")

# Sleep to ensure the data is eventually there.
time.sleep(2)

# Retrieve the contents of ``myobject``.
# print "A new file named" newkey.keyname + "has been created in your bucket. The contents are listed below."
print "An object named 'myobject' has been created in " + newbucket.name
print "Displaying 'myobject' contents - : " + newkey.get_contents_as_string()

# Delete the key.
newkey.delete()
# Delete the bucket.
newbucket.delete()
print "========================================================"
print "The bucket has been deleted after clearing its contents."
print "========================================================"
