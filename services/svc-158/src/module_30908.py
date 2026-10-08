"""Service module 30908: business logic, no crypto."""


def calculate_total_30908(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30908():
    return 'module 30908 handles orders and invoices'
