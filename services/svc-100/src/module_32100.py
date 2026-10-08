"""Service module 32100: business logic, no crypto."""


def calculate_total_32100(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32100():
    return 'module 32100 handles orders and invoices'
