__author__ = 'narendra'

import M2Crypto

def generate_and_store_key_pair(password):
    """
    Purpose:
        Generate a new pair of RSA public/private keys and save them to keydir. To increase security, use a password to protect the private key.

    Arguments:
    password: The password to protect the private key

    Return value:
        success: True if generating a password-protected key file is successful, False otherwise.

    Notes:
        - If you used any other information source to solve this task than the linked documentation (e.g. a post on StackOverflow, a blog post or a discussion in a forum), please provide the link right below:
        - additional information sources go here (e.g. https://stackoverflow.com/questions/415511/how-to-get-current-time-in-python)
    """
    keydir = "./keypair"
    Alice = M2Crypto.RSA.gen_key(1024, 65537)
    Alice.save_pub_key('Alice-public.pem')
    return False

def read_key_pair_from_files(password):
    """
    Purpose:
        Read a public and private key from a password protected file in keydir.

    Arguments:
        password: Your own password to get your key from the key file.

    Return value:
        keypair: The key pair stored in keydir if read was successful, None otherwise.

    Notes:
        - If you used any other information source to solve this task than the linked documentation (e.g. a post on StackOverflow, a blog post or a discussion in a forum), please provide the link right below:
        - additional information sources go here (e.g. https://stackoverflow.com/questions/415511/how-to-get-current-time-in-python)
    """

    keydir = "./keypair"
    Alice = M2Crypto.RSA.gen_key(1024, 65537)
    Alice.save_pub_key('Alice-public.pem')
    # This is where your code goes.
    return None

# This is to test the code for this task.
assert generate_and_store_key_pair("secretpassword")
# assert read_key_pair_from_files("secretpassword")
print "Task completed! Please continue."
