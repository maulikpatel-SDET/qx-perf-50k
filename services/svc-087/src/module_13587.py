"""Service module 13587: business logic, no crypto."""


def calculate_total_13587(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13587():
    return 'module 13587 handles orders and invoices'
