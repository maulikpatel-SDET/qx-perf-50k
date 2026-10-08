"""Service module 11702: business logic, no crypto."""


def calculate_total_11702(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11702():
    return 'module 11702 handles orders and invoices'
