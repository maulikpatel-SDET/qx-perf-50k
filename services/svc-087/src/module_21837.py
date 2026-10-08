"""Service module 21837: business logic, no crypto."""


def calculate_total_21837(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21837():
    return 'module 21837 handles orders and invoices'
