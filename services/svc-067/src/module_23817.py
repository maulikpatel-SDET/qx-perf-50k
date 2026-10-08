"""Service module 23817: business logic, no crypto."""


def calculate_total_23817(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23817():
    return 'module 23817 handles orders and invoices'
