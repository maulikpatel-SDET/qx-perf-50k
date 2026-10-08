"""Service module 21202: business logic, no crypto."""


def calculate_total_21202(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21202():
    return 'module 21202 handles orders and invoices'
