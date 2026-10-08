"""Service module 39817: business logic, no crypto."""


def calculate_total_39817(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39817():
    return 'module 39817 handles orders and invoices'
