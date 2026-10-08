"""Service module 36036: business logic, no crypto."""


def calculate_total_36036(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36036():
    return 'module 36036 handles orders and invoices'
