List all buckets, create a S3 bucket and delete the created bucket.
===============================================================================================

Prerequisites
--------------

1.  Create an **AWS** account. Learn more about AWS here http://aws.amazon.com/getting-started/

2.  Create an **IAM** user with the required permissions to perform **S3** related operations. Learn more here --> http://docs.aws.amazon.com/IAM/latest/UserGuide/GSGHowToCreateAdminsGroup.html  
	**Note**: It is advisable to assign least privileges to users.
	
3.	Create an **Access Key** and **Secret Key** for your user. It is required in **Step 7**. Learn more here http://docs.aws.amazon.com/IAM/latest/UserGuide/ManagingCredentials.html#Using_CreateAccessKey
 
4.	Make sure you have installed **Python** https://www.python.org/downloads/ . This code assumes that you will be installing version 2.x

5.  Install **Pip** from https://pip.pypa.io/en/latest/. Pip is required to to install boto. 
    Start by downloading pip from https://bootstrap.pypa.io/get-pip.py and then install it using the command ``python get-pip.py``. To upgrade pip on Linux run command ``pip install -U pip``

6.  AWS SDK for Python is called **Boto**. You can find more information here http://aws.amazon.com/sdk-for-python
    To install Boto run command ``pip install boto``. Alternatively you can install Boto from git by running :
    
    | ``git clone git://github.com/boto/boto.git``  
    | ``cd boto``  
    | ``python setup.py install``  
    
7.  Configure **Boto credentials**: Information about Boto configuration is available here - https://boto.readthedocs.org/en/latest/boto_config_tut.html. Depending on the OS you use, the configuration may vary. In Linux and MAC a file named ``/etc/boto.cfg`` for all users or ``~/.boto`` for single user has to be created. The content of the file should have the following lines. If you are using IAM roles with S3 access on an EC2 instances, this step can be ignored.
    
  | ``[Credentials]``  
  | ``aws_access_key_id = <your_access_key_here>``  
  | ``aws_secret_access_key = <your_secret_key_here>`` 

S3 bucket
-------------------    
1.  More information about S3 can be found here http://aws.amazon.com/s3

2.  To execute the downloaded code use the following command ``python s3-create-list-delete-bucket-object.py``

Support and References
----------------------
Use this script at your own risk.

a.	https://aws.amazon.com/premiumsupport/  
b.	https://www.python.org/  
c.	http://aws.amazon.com/python/  
d.	http://aws.amazon.com/sdk-for-python/  
e.	https://boto.readthedocs.org/en/latest/  
