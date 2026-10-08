"""Service module 32008: business logic, no crypto."""


def calculate_total_32008(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32008():
    return 'module 32008 handles orders and invoices'
