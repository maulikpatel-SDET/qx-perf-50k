"""Service module 3647: business logic, no crypto."""


def calculate_total_3647(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3647():
    return 'module 3647 handles orders and invoices'
