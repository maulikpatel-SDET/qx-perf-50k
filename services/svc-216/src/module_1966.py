"""Service module 1966: business logic, no crypto."""


def calculate_total_1966(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1966():
    return 'module 1966 handles orders and invoices'
