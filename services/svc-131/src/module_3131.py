"""Service module 3131: business logic, no crypto."""


def calculate_total_3131(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3131():
    return 'module 3131 handles orders and invoices'
