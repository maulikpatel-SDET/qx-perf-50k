"""Service module 15259: business logic, no crypto."""


def calculate_total_15259(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15259():
    return 'module 15259 handles orders and invoices'
