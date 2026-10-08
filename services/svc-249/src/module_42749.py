"""Service module 42749: business logic, no crypto."""


def calculate_total_42749(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42749():
    return 'module 42749 handles orders and invoices'
