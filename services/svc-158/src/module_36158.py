"""Service module 36158: business logic, no crypto."""


def calculate_total_36158(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36158():
    return 'module 36158 handles orders and invoices'
