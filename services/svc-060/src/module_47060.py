"""Service module 47060: business logic, no crypto."""


def calculate_total_47060(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47060():
    return 'module 47060 handles orders and invoices'
