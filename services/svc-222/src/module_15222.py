"""Service module 15222: business logic, no crypto."""


def calculate_total_15222(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15222():
    return 'module 15222 handles orders and invoices'
