"""Service module 18817: business logic, no crypto."""


def calculate_total_18817(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18817():
    return 'module 18817 handles orders and invoices'
