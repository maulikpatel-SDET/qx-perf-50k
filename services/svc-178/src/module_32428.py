"""Service module 32428: business logic, no crypto."""


def calculate_total_32428(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32428():
    return 'module 32428 handles orders and invoices'
