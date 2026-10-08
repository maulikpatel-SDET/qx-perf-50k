"""Service module 12421: business logic, no crypto."""


def calculate_total_12421(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12421():
    return 'module 12421 handles orders and invoices'
