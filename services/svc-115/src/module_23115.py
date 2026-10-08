"""Service module 23115: business logic, no crypto."""


def calculate_total_23115(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23115():
    return 'module 23115 handles orders and invoices'
