"""Service module 12131: business logic, no crypto."""


def calculate_total_12131(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12131():
    return 'module 12131 handles orders and invoices'
