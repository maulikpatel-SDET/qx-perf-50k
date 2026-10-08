"""Service module 16428: business logic, no crypto."""


def calculate_total_16428(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16428():
    return 'module 16428 handles orders and invoices'
