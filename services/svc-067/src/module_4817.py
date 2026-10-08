"""Service module 4817: business logic, no crypto."""


def calculate_total_4817(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4817():
    return 'module 4817 handles orders and invoices'
