"""Service module 25518: business logic, no crypto."""


def calculate_total_25518(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25518():
    return 'module 25518 handles orders and invoices'
