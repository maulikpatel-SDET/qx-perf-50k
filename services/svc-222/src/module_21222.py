"""Service module 21222: business logic, no crypto."""


def calculate_total_21222(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21222():
    return 'module 21222 handles orders and invoices'
