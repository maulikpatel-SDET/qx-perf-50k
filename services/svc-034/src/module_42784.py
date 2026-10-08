"""Service module 42784: business logic, no crypto."""


def calculate_total_42784(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42784():
    return 'module 42784 handles orders and invoices'
