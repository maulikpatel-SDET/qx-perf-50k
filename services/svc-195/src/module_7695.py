"""Service module 7695: business logic, no crypto."""


def calculate_total_7695(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7695():
    return 'module 7695 handles orders and invoices'
