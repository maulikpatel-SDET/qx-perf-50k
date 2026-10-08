"""Service module 3193: business logic, no crypto."""


def calculate_total_3193(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3193():
    return 'module 3193 handles orders and invoices'
