"""Service module 22075: business logic, no crypto."""


def calculate_total_22075(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22075():
    return 'module 22075 handles orders and invoices'
