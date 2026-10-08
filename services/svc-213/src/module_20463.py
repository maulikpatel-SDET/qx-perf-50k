"""Service module 20463: business logic, no crypto."""


def calculate_total_20463(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20463():
    return 'module 20463 handles orders and invoices'
