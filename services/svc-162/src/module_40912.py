"""Service module 40912: business logic, no crypto."""


def calculate_total_40912(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40912():
    return 'module 40912 handles orders and invoices'
