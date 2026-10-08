"""Service module 35223: business logic, no crypto."""


def calculate_total_35223(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35223():
    return 'module 35223 handles orders and invoices'
