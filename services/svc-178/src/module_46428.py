"""Service module 46428: business logic, no crypto."""


def calculate_total_46428(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46428():
    return 'module 46428 handles orders and invoices'
