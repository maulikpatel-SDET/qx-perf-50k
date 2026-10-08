"""Service module 7131: business logic, no crypto."""


def calculate_total_7131(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7131():
    return 'module 7131 handles orders and invoices'
