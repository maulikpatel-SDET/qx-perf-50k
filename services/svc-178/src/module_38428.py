"""Service module 38428: business logic, no crypto."""


def calculate_total_38428(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38428():
    return 'module 38428 handles orders and invoices'
