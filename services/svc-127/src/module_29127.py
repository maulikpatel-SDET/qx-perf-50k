"""Service module 29127: business logic, no crypto."""


def calculate_total_29127(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29127():
    return 'module 29127 handles orders and invoices'
