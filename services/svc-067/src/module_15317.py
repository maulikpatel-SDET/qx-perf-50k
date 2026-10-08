"""Service module 15317: business logic, no crypto."""


def calculate_total_15317(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15317():
    return 'module 15317 handles orders and invoices'
