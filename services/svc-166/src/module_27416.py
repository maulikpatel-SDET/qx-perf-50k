"""Service module 27416: business logic, no crypto."""


def calculate_total_27416(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27416():
    return 'module 27416 handles orders and invoices'
