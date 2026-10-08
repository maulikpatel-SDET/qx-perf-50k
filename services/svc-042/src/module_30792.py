"""Service module 30792: business logic, no crypto."""


def calculate_total_30792(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30792():
    return 'module 30792 handles orders and invoices'
