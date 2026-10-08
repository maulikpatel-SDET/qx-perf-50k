"""Service module 5483: business logic, no crypto."""


def calculate_total_5483(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5483():
    return 'module 5483 handles orders and invoices'
