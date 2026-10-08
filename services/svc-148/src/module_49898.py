"""Service module 49898: business logic, no crypto."""


def calculate_total_49898(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49898():
    return 'module 49898 handles orders and invoices'
