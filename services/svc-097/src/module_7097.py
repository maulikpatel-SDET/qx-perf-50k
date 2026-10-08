"""Service module 7097: business logic, no crypto."""


def calculate_total_7097(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7097():
    return 'module 7097 handles orders and invoices'
