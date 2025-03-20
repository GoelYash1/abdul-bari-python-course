email = input("Enter email address: ")

find_at_rate_index = email.find("@")
find_dot_index = email.rfind(".")

user_id = email[:find_at_rate_index]
domain_name = email[find_at_rate_index+1:find_dot_index]
print(
    f"user_id = {user_id}\ndomain_name = {domain_name}"
)