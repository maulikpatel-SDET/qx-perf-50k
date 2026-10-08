"""Service module 37097: business logic, no crypto."""


def calculate_total_37097(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37097():
    return 'module 37097 handles orders and invoices'
