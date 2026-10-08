"""Service module 22131: business logic, no crypto."""


def calculate_total_22131(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22131():
    return 'module 22131 handles orders and invoices'
