"""Service module 21784: business logic, no crypto."""


def calculate_total_21784(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21784():
    return 'module 21784 handles orders and invoices'
