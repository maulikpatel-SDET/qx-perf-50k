"""Service module 24187: business logic, no crypto."""


def calculate_total_24187(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24187():
    return 'module 24187 handles orders and invoices'
