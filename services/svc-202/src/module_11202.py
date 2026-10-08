"""Service module 11202: business logic, no crypto."""


def calculate_total_11202(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11202():
    return 'module 11202 handles orders and invoices'
