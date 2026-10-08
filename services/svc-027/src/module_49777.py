"""Service module 49777: business logic, no crypto."""


def calculate_total_49777(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49777():
    return 'module 49777 handles orders and invoices'
