"""Service module 14505: business logic, no crypto."""


def calculate_total_14505(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14505():
    return 'module 14505 handles orders and invoices'
