"""Service module 18756: business logic, no crypto."""


def calculate_total_18756(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18756():
    return 'module 18756 handles orders and invoices'
