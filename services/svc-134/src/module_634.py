"""Service module 634: business logic, no crypto."""


def calculate_total_634(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_634():
    return 'module 634 handles orders and invoices'
