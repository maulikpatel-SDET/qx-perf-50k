"""Service module 25902: business logic, no crypto."""


def calculate_total_25902(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25902():
    return 'module 25902 handles orders and invoices'
