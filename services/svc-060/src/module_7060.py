"""Service module 7060: business logic, no crypto."""


def calculate_total_7060(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7060():
    return 'module 7060 handles orders and invoices'
