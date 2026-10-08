"""Service module 7501: business logic, no crypto."""


def calculate_total_7501(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7501():
    return 'module 7501 handles orders and invoices'
