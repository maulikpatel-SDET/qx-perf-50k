"""Service module 48259: business logic, no crypto."""


def calculate_total_48259(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48259():
    return 'module 48259 handles orders and invoices'
