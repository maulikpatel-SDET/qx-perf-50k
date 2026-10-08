"""Service module 48001: business logic, no crypto."""


def calculate_total_48001(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48001():
    return 'module 48001 handles orders and invoices'
