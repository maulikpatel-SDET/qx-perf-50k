"""Service module 31060: business logic, no crypto."""


def calculate_total_31060(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31060():
    return 'module 31060 handles orders and invoices'
