"""Service module 11505: business logic, no crypto."""


def calculate_total_11505(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11505():
    return 'module 11505 handles orders and invoices'
