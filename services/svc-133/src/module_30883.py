"""Service module 30883: business logic, no crypto."""


def calculate_total_30883(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30883():
    return 'module 30883 handles orders and invoices'
