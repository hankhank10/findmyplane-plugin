# Import the library at the start of your script
import findmyplane_plugin

# You can create a new plane instance from the server by calling request_new_plane_instance
# This also accepts two variables: plane name and atc code, but these are optional
findmyplane_plugin.request_new_plane_instance("F-14 Tomcat", "MAVERICK", "My Super Cool App")

# We can check whether we have got a plane listance loaded by calling connection_status
# This will return either "disconnected" or the ident public key
if findmyplane_plugin.connection_status() != "connected":
    print ("Looks like something went wrong creating the instance")
    # You would probably want to incorporate a loop here to re-request an instance...
    # ... or display an error message to the user asking them to try again
    # For this simple example, however, we will just:
    exit()

if findmyplane_plugin.connection_status() == "connected":
    print ("Connected to server!")

# We can get the keys by using variables
print ("Public ident key is", findmyplane_plugin.ident_public_key)
print ("Private ident key is", findmyplane_plugin.ident_private_key, "not that you as a user would care about this")

# We can also get an easy link url
print ("You can view your plane at", findmyplane_plugin.url_to_view())


# Now it is time to set the location of our plane.
# In reality you would want to do this many times to keep the plane moving.
findmyplane_plugin.set_plane_location(51.5074, -0.1278, 90, 1000)

# Alternatively if you want to check whether a datapoint has been sent you can:
if findmyplane_plugin.set_plane_location(51.5074, -0.1278, 90, 5000) == "success":
    print ("Successfully sent datapoint to server and got success back")

if findmyplane_plugin.set_plane_location(51.5074, -0.1278, 90, 7000, 200) != "success":
    print ("Well something went wrong sending that datapoint...")


# It is optional, but you can also disconnect from the instance if you want to
# This would be useful, for instance, if you want to start a new flight
findmyplane_plugin.disconnect_from_plane_instance()
