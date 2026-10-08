"""Service module 38060: business logic, no crypto."""


def calculate_total_38060(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38060():
    return 'module 38060 handles orders and invoices'
