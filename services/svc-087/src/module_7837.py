"""Service module 7837: business logic, no crypto."""


def calculate_total_7837(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7837():
    return 'module 7837 handles orders and invoices'
