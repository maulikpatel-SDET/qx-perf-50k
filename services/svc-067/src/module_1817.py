"""Service module 1817: business logic, no crypto."""


def calculate_total_1817(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1817():
    return 'module 1817 handles orders and invoices'
