"""Service module 30777: business logic, no crypto."""


def calculate_total_30777(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30777():
    return 'module 30777 handles orders and invoices'
