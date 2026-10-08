"""Service module 24558: business logic, no crypto."""


def calculate_total_24558(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24558():
    return 'module 24558 handles orders and invoices'
