"""Service module 17193: business logic, no crypto."""


def calculate_total_17193(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17193():
    return 'module 17193 handles orders and invoices'
