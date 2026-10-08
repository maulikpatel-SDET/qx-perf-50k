"""Service module 25797: business logic, no crypto."""


def calculate_total_25797(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25797():
    return 'module 25797 handles orders and invoices'
