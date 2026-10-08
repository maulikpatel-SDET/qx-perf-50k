"""Service module 45453: business logic, no crypto."""


def calculate_total_45453(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45453():
    return 'module 45453 handles orders and invoices'
