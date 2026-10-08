"""Service module 19498: business logic, no crypto."""


def calculate_total_19498(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19498():
    return 'module 19498 handles orders and invoices'
