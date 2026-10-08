"""Service module 21842: business logic, no crypto."""


def calculate_total_21842(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21842():
    return 'module 21842 handles orders and invoices'
