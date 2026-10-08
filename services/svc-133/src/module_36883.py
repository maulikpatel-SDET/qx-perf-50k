"""Service module 36883: business logic, no crypto."""


def calculate_total_36883(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36883():
    return 'module 36883 handles orders and invoices'
