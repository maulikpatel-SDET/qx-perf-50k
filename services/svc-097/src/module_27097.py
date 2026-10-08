"""Service module 27097: business logic, no crypto."""


def calculate_total_27097(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27097():
    return 'module 27097 handles orders and invoices'
