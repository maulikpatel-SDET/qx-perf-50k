"""Service module 29299: business logic, no crypto."""


def calculate_total_29299(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29299():
    return 'module 29299 handles orders and invoices'
