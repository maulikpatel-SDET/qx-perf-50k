"""Service module 8224: business logic, no crypto."""


def calculate_total_8224(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8224():
    return 'module 8224 handles orders and invoices'
