"""Service module 29803: business logic, no crypto."""


def calculate_total_29803(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29803():
    return 'module 29803 handles orders and invoices'
