"""Service module 20949: business logic, no crypto."""


def calculate_total_20949(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20949():
    return 'module 20949 handles orders and invoices'
