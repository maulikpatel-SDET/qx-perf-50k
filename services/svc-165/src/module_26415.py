"""Service module 26415: business logic, no crypto."""


def calculate_total_26415(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26415():
    return 'module 26415 handles orders and invoices'
