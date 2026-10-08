"""Service module 15399: business logic, no crypto."""


def calculate_total_15399(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15399():
    return 'module 15399 handles orders and invoices'
