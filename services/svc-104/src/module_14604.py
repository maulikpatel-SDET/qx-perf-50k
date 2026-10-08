"""Service module 14604: business logic, no crypto."""


def calculate_total_14604(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14604():
    return 'module 14604 handles orders and invoices'
