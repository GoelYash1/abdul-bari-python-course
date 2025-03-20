card_no = int(input("Enter Card num: "))
card_string = str(card_no)

card_num = " ".join([card_string[i:i+4] for i in range(0, len(card_string),4)])

last_digits = card_num[15::]
four = "*"*4+" "

disp_card_details = four * 3 + last_digits
print(disp_card_details)

