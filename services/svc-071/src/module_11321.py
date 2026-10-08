"""Service module 11321: business logic, no crypto."""


def calculate_total_11321(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11321():
    return 'module 11321 handles orders and invoices'
