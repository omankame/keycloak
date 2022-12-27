import json

with open (
     "/home/onkar/keycloak/roles/keycloak/files/realm_role.json"
) as f:

    data = json.load
    list1 = list((p_id.get("id") for p_id in data if p_id.get("name") == "pf_users"))
    print(*list1, sep="/n")
