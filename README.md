# venkman
Service Account / Logged In User Enumeration


**Pip Install Instructions**

Note: To test if pip is already installed execute.

`pip -V`

(1) Mac and Kali users can simply use the following command to download and install `pip`.

`curl https://bootstrap.pypa.io/get-pip.py -o - | python`

**Venkman Install Instructions**

Venkman requires the 'wmic' client and the 'rpcclient', these are both installed by default on Kali Linux. If you want to run the tool on any other Unix/Linux platform it should work as long as they are installed and in the env path.

(1) Once `pip` has successfully downloaded and installed, we can install Venkman:

`sudo pip install venkman`

(2) You should now be able to execute 'venkman' from any working directory in any terminal.
 
`venkman`
