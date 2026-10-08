"""Service module 40202: business logic, no crypto."""


def calculate_total_40202(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40202():
    return 'module 40202 handles orders and invoices'
