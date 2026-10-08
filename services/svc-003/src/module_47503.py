"""Service module 47503: business logic, no crypto."""


def calculate_total_47503(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47503():
    return 'module 47503 handles orders and invoices'
