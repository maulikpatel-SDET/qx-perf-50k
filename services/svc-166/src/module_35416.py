"""Service module 35416: business logic, no crypto."""


def calculate_total_35416(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35416():
    return 'module 35416 handles orders and invoices'
