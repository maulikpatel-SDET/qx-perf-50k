"""Service module 39823: business logic, no crypto."""


def calculate_total_39823(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39823():
    return 'module 39823 handles orders and invoices'
