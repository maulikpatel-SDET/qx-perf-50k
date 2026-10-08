"""Service module 23708: business logic, no crypto."""


def calculate_total_23708(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23708():
    return 'module 23708 handles orders and invoices'
