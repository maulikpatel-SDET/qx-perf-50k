"""Service module 9399: business logic, no crypto."""


def calculate_total_9399(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9399():
    return 'module 9399 handles orders and invoices'
