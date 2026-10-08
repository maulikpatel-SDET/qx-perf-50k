"""Service module 7777: business logic, no crypto."""


def calculate_total_7777(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7777():
    return 'module 7777 handles orders and invoices'
