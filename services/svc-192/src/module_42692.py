"""Service module 42692: business logic, no crypto."""


def calculate_total_42692(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42692():
    return 'module 42692 handles orders and invoices'
