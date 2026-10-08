"""Service module 41817: business logic, no crypto."""


def calculate_total_41817(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41817():
    return 'module 41817 handles orders and invoices'
