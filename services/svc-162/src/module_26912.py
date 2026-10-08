"""Service module 26912: business logic, no crypto."""


def calculate_total_26912(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26912():
    return 'module 26912 handles orders and invoices'
