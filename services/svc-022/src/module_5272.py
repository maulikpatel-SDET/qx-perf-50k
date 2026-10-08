"""Service module 5272: business logic, no crypto."""


def calculate_total_5272(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5272():
    return 'module 5272 handles orders and invoices'
