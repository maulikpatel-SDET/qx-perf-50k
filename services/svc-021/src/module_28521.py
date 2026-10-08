"""Service module 28521: business logic, no crypto."""


def calculate_total_28521(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28521():
    return 'module 28521 handles orders and invoices'
