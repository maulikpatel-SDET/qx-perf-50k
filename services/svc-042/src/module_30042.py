"""Service module 30042: business logic, no crypto."""


def calculate_total_30042(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30042():
    return 'module 30042 handles orders and invoices'
