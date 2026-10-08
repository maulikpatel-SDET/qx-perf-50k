"""Service module 3505: business logic, no crypto."""


def calculate_total_3505(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3505():
    return 'module 3505 handles orders and invoices'
