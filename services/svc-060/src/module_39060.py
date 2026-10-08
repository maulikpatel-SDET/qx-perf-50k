"""Service module 39060: business logic, no crypto."""


def calculate_total_39060(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39060():
    return 'module 39060 handles orders and invoices'
