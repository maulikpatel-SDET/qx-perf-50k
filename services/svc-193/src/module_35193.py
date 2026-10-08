"""Service module 35193: business logic, no crypto."""


def calculate_total_35193(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35193():
    return 'module 35193 handles orders and invoices'
