"""Service module 25150: business logic, no crypto."""


def calculate_total_25150(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25150():
    return 'module 25150 handles orders and invoices'
