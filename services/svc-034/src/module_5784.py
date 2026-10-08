"""Service module 5784: business logic, no crypto."""


def calculate_total_5784(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5784():
    return 'module 5784 handles orders and invoices'
