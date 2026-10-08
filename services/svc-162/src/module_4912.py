"""Service module 4912: business logic, no crypto."""


def calculate_total_4912(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4912():
    return 'module 4912 handles orders and invoices'
