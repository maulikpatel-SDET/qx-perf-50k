"""Service module 46416: business logic, no crypto."""


def calculate_total_46416(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46416():
    return 'module 46416 handles orders and invoices'
