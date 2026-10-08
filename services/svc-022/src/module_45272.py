"""Service module 45272: business logic, no crypto."""


def calculate_total_45272(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45272():
    return 'module 45272 handles orders and invoices'
