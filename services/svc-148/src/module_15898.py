"""Service module 15898: business logic, no crypto."""


def calculate_total_15898(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15898():
    return 'module 15898 handles orders and invoices'
