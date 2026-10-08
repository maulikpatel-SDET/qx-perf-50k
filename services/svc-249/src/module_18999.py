"""Service module 18999: business logic, no crypto."""


def calculate_total_18999(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18999():
    return 'module 18999 handles orders and invoices'
