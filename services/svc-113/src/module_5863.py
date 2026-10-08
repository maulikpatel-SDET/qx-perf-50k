"""Service module 5863: business logic, no crypto."""


def calculate_total_5863(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5863():
    return 'module 5863 handles orders and invoices'
