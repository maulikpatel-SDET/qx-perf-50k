"""Service module 36647: business logic, no crypto."""


def calculate_total_36647(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36647():
    return 'module 36647 handles orders and invoices'
