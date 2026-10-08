"""Service module 44451: business logic, no crypto."""


def calculate_total_44451(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44451():
    return 'module 44451 handles orders and invoices'
