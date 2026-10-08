"""Service module 18415: business logic, no crypto."""


def calculate_total_18415(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18415():
    return 'module 18415 handles orders and invoices'
