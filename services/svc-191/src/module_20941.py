"""Service module 20941: business logic, no crypto."""


def calculate_total_20941(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20941():
    return 'module 20941 handles orders and invoices'
