"""Service module 35272: business logic, no crypto."""


def calculate_total_35272(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35272():
    return 'module 35272 handles orders and invoices'
