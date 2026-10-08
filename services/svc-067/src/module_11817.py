"""Service module 11817: business logic, no crypto."""


def calculate_total_11817(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11817():
    return 'module 11817 handles orders and invoices'
