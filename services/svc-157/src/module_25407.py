"""Service module 25407: business logic, no crypto."""


def calculate_total_25407(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25407():
    return 'module 25407 handles orders and invoices'
