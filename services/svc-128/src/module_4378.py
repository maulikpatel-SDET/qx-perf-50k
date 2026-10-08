"""Service module 4378: business logic, no crypto."""


def calculate_total_4378(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4378():
    return 'module 4378 handles orders and invoices'
