"""Service module 37708: business logic, no crypto."""


def calculate_total_37708(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37708():
    return 'module 37708 handles orders and invoices'
