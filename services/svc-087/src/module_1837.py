"""Service module 1837: business logic, no crypto."""


def calculate_total_1837(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1837():
    return 'module 1837 handles orders and invoices'
