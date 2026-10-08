"""Service module 13383: business logic, no crypto."""


def calculate_total_13383(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13383():
    return 'module 13383 handles orders and invoices'
