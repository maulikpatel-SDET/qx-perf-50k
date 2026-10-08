"""Service module 9517: business logic, no crypto."""


def calculate_total_9517(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9517():
    return 'module 9517 handles orders and invoices'
