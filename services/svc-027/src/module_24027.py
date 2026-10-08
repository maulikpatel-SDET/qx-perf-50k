"""Service module 24027: business logic, no crypto."""


def calculate_total_24027(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24027():
    return 'module 24027 handles orders and invoices'
