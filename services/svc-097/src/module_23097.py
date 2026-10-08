"""Service module 23097: business logic, no crypto."""


def calculate_total_23097(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23097():
    return 'module 23097 handles orders and invoices'
