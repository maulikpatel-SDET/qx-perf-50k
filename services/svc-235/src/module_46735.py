"""Service module 46735: business logic, no crypto."""


def calculate_total_46735(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46735():
    return 'module 46735 handles orders and invoices'
