"""Service module 1272: business logic, no crypto."""


def calculate_total_1272(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1272():
    return 'module 1272 handles orders and invoices'
