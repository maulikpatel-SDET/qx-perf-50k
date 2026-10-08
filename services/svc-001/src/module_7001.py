"""Service module 7001: business logic, no crypto."""


def calculate_total_7001(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7001():
    return 'module 7001 handles orders and invoices'
