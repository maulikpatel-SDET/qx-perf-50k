"""Service module 49991: business logic, no crypto."""


def calculate_total_49991(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49991():
    return 'module 49991 handles orders and invoices'
