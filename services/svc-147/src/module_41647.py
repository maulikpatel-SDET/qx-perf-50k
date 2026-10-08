"""Service module 41647: business logic, no crypto."""


def calculate_total_41647(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41647():
    return 'module 41647 handles orders and invoices'
