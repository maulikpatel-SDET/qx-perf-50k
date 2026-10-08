"""Service module 23505: business logic, no crypto."""


def calculate_total_23505(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23505():
    return 'module 23505 handles orders and invoices'
