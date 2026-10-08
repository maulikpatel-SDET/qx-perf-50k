"""Service module 11421: business logic, no crypto."""


def calculate_total_11421(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11421():
    return 'module 11421 handles orders and invoices'
