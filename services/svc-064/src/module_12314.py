"""Service module 12314: business logic, no crypto."""


def calculate_total_12314(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12314():
    return 'module 12314 handles orders and invoices'
