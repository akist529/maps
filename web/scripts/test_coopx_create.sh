#!/bin/bash

# PREPARE HELP MESSAGE
show_help() {
    echo
    echo $0 - shows how to login to backend and send a coop create proposal.
    echo 
    echo "Usage: $0 -u USERNAME -p PASSWORD"
    echo
    echo "Options:"
    echo "  -u    Specify the username"
    echo "  -p    Specify the password"
    echo "  -h    Display this help message and exit"
}

# VALIDATE USER INPUTS
username_provided=0
password_provided=0
while getopts ":u:p:h:" option; do
   case $option in
        u) # Input username
            username=$OPTARG
            username_provided=1;;
        p) # Input password
            password=$OPTARG
            password_provided=1;;
        h) # Show Help
            show_help
            exit 0;;
        \?) # Invalid option
            echo "Error: Invalid option"
            show_help
            exit 1;;
   esac
done
if [ $username_provided -eq 0 ]; then
    echo "Error: Username (-u) is required."
    show_help
    exit 1
fi

if [ $password_provided -eq 0 ]; then
    echo "Error: Password (-p) is required."
    show_help
    exit 1
fi

#=============================================================================

# API CALL 1: LOGIN
login_req_json=$(cat << EOF
{
  "username": "maxgraziano",
  "password": "password"
}
EOF
)
url="http://localhost:8000/api/token/"

login_response=$( curl -s -X POST "$url" -H "Content-type: application/json" -d "$login_req_json" )
access_token=$( echo "$login_response" | jq -r '.access' )  # Extract "access" value from response json.

# API CALL 2: SEND CREATE PROPOSAL
create_coop_req_json=$(cat << EOF
{
  "name": "Test Max 9999",
  "web_site": "http://www.1871.com/",
  "description": "My Coop Description",
  "is_public": true, 
  "scope": "Testing", 
  "tags": "tag1, tag2, tag3"
}
EOF
)
url="http://localhost:8000/coopx/create/"
access_header="Authorization: Bearer "$access_token""
create_coop_response=$( curl -s -X POST "$url" -H "$access_header" -H "Content-type: application/json" -d "$create_coop_req_json" )
echo $create_coop_response