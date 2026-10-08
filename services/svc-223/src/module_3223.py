"""Service module 3223: business logic, no crypto."""


def calculate_total_3223(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3223():
    return 'module 3223 handles orders and invoices'
