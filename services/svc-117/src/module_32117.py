"""Service module 32117: business logic, no crypto."""


def calculate_total_32117(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32117():
    return 'module 32117 handles orders and invoices'
