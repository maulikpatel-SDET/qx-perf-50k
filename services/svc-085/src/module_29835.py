"""Service module 29835: business logic, no crypto."""


def calculate_total_29835(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29835():
    return 'module 29835 handles orders and invoices'
