"""Service module 21647: business logic, no crypto."""


def calculate_total_21647(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21647():
    return 'module 21647 handles orders and invoices'
