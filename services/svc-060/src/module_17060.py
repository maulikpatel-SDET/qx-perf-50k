"""Service module 17060: business logic, no crypto."""


def calculate_total_17060(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17060():
    return 'module 17060 handles orders and invoices'
