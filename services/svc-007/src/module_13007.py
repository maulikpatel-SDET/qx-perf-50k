"""Service module 13007: business logic, no crypto."""


def calculate_total_13007(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13007():
    return 'module 13007 handles orders and invoices'
