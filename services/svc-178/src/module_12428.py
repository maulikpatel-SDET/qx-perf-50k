"""Service module 12428: business logic, no crypto."""


def calculate_total_12428(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12428():
    return 'module 12428 handles orders and invoices'
