"""Service module 16767: business logic, no crypto."""


def calculate_total_16767(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16767():
    return 'module 16767 handles orders and invoices'
