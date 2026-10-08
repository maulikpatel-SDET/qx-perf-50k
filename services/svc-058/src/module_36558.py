"""Service module 36558: business logic, no crypto."""


def calculate_total_36558(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36558():
    return 'module 36558 handles orders and invoices'
