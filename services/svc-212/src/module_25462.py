"""Service module 25462: business logic, no crypto."""


def calculate_total_25462(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25462():
    return 'module 25462 handles orders and invoices'
