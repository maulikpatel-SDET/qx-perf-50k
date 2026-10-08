"""Service module 4846: business logic, no crypto."""


def calculate_total_4846(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4846():
    return 'module 4846 handles orders and invoices'
