"""Service module 42828: business logic, no crypto."""


def calculate_total_42828(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42828():
    return 'module 42828 handles orders and invoices'
