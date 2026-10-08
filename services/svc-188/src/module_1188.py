"""Service module 1188: business logic, no crypto."""


def calculate_total_1188(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1188():
    return 'module 1188 handles orders and invoices'
