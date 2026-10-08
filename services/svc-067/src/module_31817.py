"""Service module 31817: business logic, no crypto."""


def calculate_total_31817(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31817():
    return 'module 31817 handles orders and invoices'
