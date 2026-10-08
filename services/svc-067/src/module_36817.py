"""Service module 36817: business logic, no crypto."""


def calculate_total_36817(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36817():
    return 'module 36817 handles orders and invoices'
