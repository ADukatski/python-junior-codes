avio_name = input()
number_of_tickets_for_adult = int(input())
number_of_tickets_for_kids = int(input())
net_price_adult = float(input())
service_tax = float(input())

net_price_kid = net_price_adult - (net_price_adult * 0.70)
end_price_with_tax_adult = net_price_adult + service_tax
end_price_with_tax_kids = net_price_kid + service_tax
total_price_tickets = (number_of_tickets_for_adult * end_price_with_tax_adult) \
                      + (end_price_with_tax_kids * number_of_tickets_for_kids)
total = total_price_tickets * 0.20


print(f"The profit of your agency from {avio_name} tickets is {total:.2f} lv.")
