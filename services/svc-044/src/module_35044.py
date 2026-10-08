"""Service module 35044: business logic, no crypto."""


def calculate_total_35044(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35044():
    return 'module 35044 handles orders and invoices'
