"""Service module 37554: business logic, no crypto."""


def calculate_total_37554(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37554():
    return 'module 37554 handles orders and invoices'
