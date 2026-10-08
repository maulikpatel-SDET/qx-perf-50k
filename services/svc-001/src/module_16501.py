"""Service module 16501: business logic, no crypto."""


def calculate_total_16501(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16501():
    return 'module 16501 handles orders and invoices'
