"""Service module 25817: business logic, no crypto."""


def calculate_total_25817(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25817():
    return 'module 25817 handles orders and invoices'
