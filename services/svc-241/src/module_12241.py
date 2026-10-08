"""Service module 12241: business logic, no crypto."""


def calculate_total_12241(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12241():
    return 'module 12241 handles orders and invoices'
