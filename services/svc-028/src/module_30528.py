"""Service module 30528: business logic, no crypto."""


def calculate_total_30528(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30528():
    return 'module 30528 handles orders and invoices'
