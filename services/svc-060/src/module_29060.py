"""Service module 29060: business logic, no crypto."""


def calculate_total_29060(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29060():
    return 'module 29060 handles orders and invoices'
