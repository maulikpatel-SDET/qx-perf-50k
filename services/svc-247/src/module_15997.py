"""Service module 15997: business logic, no crypto."""


def calculate_total_15997(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15997():
    return 'module 15997 handles orders and invoices'
