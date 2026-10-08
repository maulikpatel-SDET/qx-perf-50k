"""Service module 39676: business logic, no crypto."""


def calculate_total_39676(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39676():
    return 'module 39676 handles orders and invoices'
