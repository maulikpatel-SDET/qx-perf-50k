"""Service module 2272: business logic, no crypto."""


def calculate_total_2272(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2272():
    return 'module 2272 handles orders and invoices'
