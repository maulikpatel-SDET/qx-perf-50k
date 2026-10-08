"""Service module 17883: business logic, no crypto."""


def calculate_total_17883(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17883():
    return 'module 17883 handles orders and invoices'
