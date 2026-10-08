"""Service module 38463: business logic, no crypto."""


def calculate_total_38463(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38463():
    return 'module 38463 handles orders and invoices'
