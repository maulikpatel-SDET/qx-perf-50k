"""Service module 12883: business logic, no crypto."""


def calculate_total_12883(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12883():
    return 'module 12883 handles orders and invoices'
