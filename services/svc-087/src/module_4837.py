"""Service module 4837: business logic, no crypto."""


def calculate_total_4837(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4837():
    return 'module 4837 handles orders and invoices'
