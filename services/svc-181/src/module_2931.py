"""Service module 2931: business logic, no crypto."""


def calculate_total_2931(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2931():
    return 'module 2931 handles orders and invoices'
