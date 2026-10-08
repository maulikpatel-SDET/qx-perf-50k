"""Service module 4798: business logic, no crypto."""


def calculate_total_4798(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4798():
    return 'module 4798 handles orders and invoices'
