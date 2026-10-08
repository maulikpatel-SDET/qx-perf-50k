"""Service module 647: business logic, no crypto."""


def calculate_total_647(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_647():
    return 'module 647 handles orders and invoices'
