"""Service module 16587: business logic, no crypto."""


def calculate_total_16587(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16587():
    return 'module 16587 handles orders and invoices'
