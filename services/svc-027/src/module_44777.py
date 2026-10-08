"""Service module 44777: business logic, no crypto."""


def calculate_total_44777(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44777():
    return 'module 44777 handles orders and invoices'
