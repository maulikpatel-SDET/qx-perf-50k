"""Service module 33784: business logic, no crypto."""


def calculate_total_33784(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33784():
    return 'module 33784 handles orders and invoices'
