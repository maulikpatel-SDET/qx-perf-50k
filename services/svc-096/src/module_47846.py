"""Service module 47846: business logic, no crypto."""


def calculate_total_47846(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47846():
    return 'module 47846 handles orders and invoices'
