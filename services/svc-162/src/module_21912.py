"""Service module 21912: business logic, no crypto."""


def calculate_total_21912(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21912():
    return 'module 21912 handles orders and invoices'
