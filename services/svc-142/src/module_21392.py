"""Service module 21392: business logic, no crypto."""


def calculate_total_21392(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21392():
    return 'module 21392 handles orders and invoices'
