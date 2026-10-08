"""Service module 30421: business logic, no crypto."""


def calculate_total_30421(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30421():
    return 'module 30421 handles orders and invoices'
