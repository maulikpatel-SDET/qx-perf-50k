"""Service module 1466: business logic, no crypto."""


def calculate_total_1466(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1466():
    return 'module 1466 handles orders and invoices'
