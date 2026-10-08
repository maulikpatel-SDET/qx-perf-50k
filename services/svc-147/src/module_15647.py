"""Service module 15647: business logic, no crypto."""


def calculate_total_15647(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15647():
    return 'module 15647 handles orders and invoices'
