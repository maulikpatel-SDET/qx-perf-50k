"""Service module 21001: business logic, no crypto."""


def calculate_total_21001(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21001():
    return 'module 21001 handles orders and invoices'
