"""Service module 38912: business logic, no crypto."""


def calculate_total_38912(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38912():
    return 'module 38912 handles orders and invoices'
