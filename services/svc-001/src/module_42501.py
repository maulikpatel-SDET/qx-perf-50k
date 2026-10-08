"""Service module 42501: business logic, no crypto."""


def calculate_total_42501(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42501():
    return 'module 42501 handles orders and invoices'
