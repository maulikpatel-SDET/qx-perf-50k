"""Service module 38001: business logic, no crypto."""


def calculate_total_38001(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38001():
    return 'module 38001 handles orders and invoices'
