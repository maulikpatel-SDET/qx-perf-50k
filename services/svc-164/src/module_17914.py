"""Service module 17914: business logic, no crypto."""


def calculate_total_17914(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17914():
    return 'module 17914 handles orders and invoices'
