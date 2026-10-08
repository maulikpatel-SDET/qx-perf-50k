"""Service module 49097: business logic, no crypto."""


def calculate_total_49097(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49097():
    return 'module 49097 handles orders and invoices'
