"""Service module 20060: business logic, no crypto."""


def calculate_total_20060(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20060():
    return 'module 20060 handles orders and invoices'
