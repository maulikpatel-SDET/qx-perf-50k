"""Service module 9692: business logic, no crypto."""


def calculate_total_9692(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9692():
    return 'module 9692 handles orders and invoices'
