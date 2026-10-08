"""Service module 36528: business logic, no crypto."""


def calculate_total_36528(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36528():
    return 'module 36528 handles orders and invoices'
