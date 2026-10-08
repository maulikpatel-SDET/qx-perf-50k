"""Service module 31708: business logic, no crypto."""


def calculate_total_31708(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31708():
    return 'module 31708 handles orders and invoices'
