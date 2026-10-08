"""Service module 1202: business logic, no crypto."""


def calculate_total_1202(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1202():
    return 'module 1202 handles orders and invoices'
