"""Service module 7376: business logic, no crypto."""


def calculate_total_7376(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7376():
    return 'module 7376 handles orders and invoices'
